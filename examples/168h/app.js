const dayNames = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
const categories = ["sleep", "work", "life", "focus", "free"];
const categoryNames = { sleep: "Sleep", work: "Work", life: "Life", focus: "Focus", free: "Available" };
const pixelsPerHour = 24;
const calendar = document.querySelector("#calendar");
const mobilePlanner = document.querySelector("#mobile-planner");
const dialog = document.querySelector("#task-dialog");
const form = document.querySelector("#task-form");
let weekStart = mondayOf(new Date());
let tasks = loadTasks();
let selectedDay = Math.max(0, Math.min(6, (new Date().getDay() + 6) % 7));

for (let hour = 0; hour < 24; hour += 0.5) {
  const option = document.createElement("option");
  option.value = String(hour);
  option.textContent = formatTime(hour);
  document.querySelector("#task-start").append(option);
}

document.querySelector("#previous-week").addEventListener("click", () => changeWeek(-7));
document.querySelector("#next-week").addEventListener("click", () => changeWeek(7));
document.querySelector("#this-week").addEventListener("click", () => {
  weekStart = mondayOf(new Date());
  tasks = loadTasks();
  render();
});
document.querySelector("#add-task").addEventListener("click", () => openTask());
document.querySelector("#add-backlog").addEventListener("click", () => openTask());
document.querySelector("#close-dialog").addEventListener("click", () => dialog.close());
document.querySelector("#cancel-task").addEventListener("click", () => dialog.close());
document.querySelector("#task-day").addEventListener("change", updateTimeField);
document.querySelector("#task-duration").addEventListener("change", () => renderSlotSuggestions());
document.querySelector("#task-start").addEventListener("change", () => renderSlotSuggestions());
form.addEventListener("input", () => { document.querySelector("#form-error").hidden = true; });
document.querySelector("#keep-backlog").addEventListener("click", () => {
  document.querySelector("#task-day").value = "";
  updateTimeField();
  form.requestSubmit();
});
document.querySelector("#slot-suggestions").addEventListener("click", event => {
  const slot = event.target.closest("[data-slot-day]");
  if (!slot) return;
  document.querySelector("#task-day").value = slot.dataset.slotDay;
  document.querySelector("#task-start").value = slot.dataset.slotStart;
  document.querySelector("#form-error").hidden = true;
  updateTimeField();
});
document.querySelector("#delete-task").addEventListener("click", () => {
  tasks = tasks.filter(task => task.id !== form.dataset.id);
  saveTasks();
  dialog.close();
  render();
});
form.addEventListener("submit", saveTask);
calendar.addEventListener("click", event => {
  const block = event.target.closest("[data-task-id]");
  if (block) openTask(tasks.find(task => task.id === block.dataset.taskId));
});
mobilePlanner.addEventListener("click", event => {
  const day = event.target.closest("[data-select-day]");
  if (day) {
    selectedDay = Number(day.dataset.selectDay);
    renderMobilePlanner();
    return;
  }
  const task = event.target.closest("[data-task-id]");
  if (task) {
    openTask(tasks.find(item => item.id === task.dataset.taskId));
    return;
  }
  const slot = event.target.closest("[data-free-start]");
  if (slot) openTask(undefined, { day: selectedDay, start: Number(slot.dataset.freeStart), duration: Math.min(1, Number(slot.dataset.freeDuration)) });
});
document.querySelector("#backlog-items").addEventListener("click", event => {
  const row = event.target.closest("[data-task-id]");
  if (row) openTask(tasks.find(task => task.id === row.dataset.taskId));
});

render();

function changeWeek(days) {
  weekStart.setDate(weekStart.getDate() + days);
  tasks = loadTasks();
  render();
}

function render() {
  const end = new Date(weekStart);
  end.setDate(end.getDate() + 6);
  document.querySelector("#week-label").textContent = `${shortDate(weekStart)} – ${shortDate(end)}`;
  renderCalendar();
  renderMobilePlanner();
  renderLedger();
  renderBacklog();
}

function renderMobilePlanner() {
  mobilePlanner.replaceChildren();
  const hours = categoryHours();
  const overview = document.createElement("div");
  overview.className = "mobile-overview";
  overview.innerHTML = `<div><span class="eyebrow">This week</span><strong>168h</strong></div><div><strong>${formatHours(hours.free)}</strong><span>available</span></div>`;
  mobilePlanner.append(overview);
  const budgetBar = document.createElement("div");
  budgetBar.className = "mobile-budget-bar";
  budgetBar.setAttribute("role", "img");
  budgetBar.setAttribute("aria-label", categories.map(category => `${categoryNames[category]} ${formatHours(hours[category])}`).join(", "));
  for (const category of categories) {
    const segment = document.createElement("span");
    segment.className = category;
    segment.style.width = `${hours[category] / 168 * 100}%`;
    budgetBar.append(segment);
  }
  mobilePlanner.append(budgetBar);
  const legend = document.createElement("div");
  legend.className = "mobile-budget-legend";
  for (const category of categories.slice(0, -1)) {
    const item = document.createElement("span");
    item.innerHTML = `<span class="swatch ${category}"></span>${categoryNames[category]} ${formatHours(hours[category])}`;
    legend.append(item);
  }
  mobilePlanner.append(legend);
  const strip = document.createElement("div");
  strip.className = "mobile-week-strip";
  strip.setAttribute("aria-label", "Choose a day in this week");
  for (let day = 0; day < 7; day++) {
    const date = new Date(weekStart);
    date.setDate(date.getDate() + day);
    const dayTasks = tasks.filter(task => task.day === day);
    const free = 24 - dayTasks.reduce((sum, task) => sum + task.duration, 0);
    const button = document.createElement("button");
    button.type = "button";
    button.className = `mobile-day-button${day === selectedDay ? " selected" : ""}`;
    button.dataset.selectDay = String(day);
    button.setAttribute("aria-pressed", String(day === selectedDay));
    button.setAttribute("aria-label", `${dayNames[day]} ${shortDate(date)}, ${formatHours(free)} available`);
    button.innerHTML = `<span>${dayNames[day]}</span><strong>${date.getDate()}</strong><small>${formatHours(free)} free</small>`;
    strip.append(button);
  }
  mobilePlanner.append(strip);
  const date = new Date(weekStart);
  date.setDate(date.getDate() + selectedDay);
  const scheduled = tasks.filter(task => task.day === selectedDay).sort((a, b) => a.start - b.start);
  const free = 24 - scheduled.reduce((sum, task) => sum + task.duration, 0);
  const heading = document.createElement("div");
  heading.className = "mobile-day-heading";
  heading.innerHTML = `<h3>${date.toLocaleDateString("en-US", { weekday: "long", month: "short", day: "numeric" })}</h3><span>${formatHours(free)} available</span>`;
  mobilePlanner.append(heading);
  const list = document.createElement("div");
  list.className = "mobile-day-list";
  let previousEnd = 0;
  for (const task of scheduled) {
    if (task.start > previousEnd) list.append(mobileFreeSlot(previousEnd, task.start));
    const block = document.createElement("button");
    block.type = "button";
    block.className = `mobile-event ${task.category}${task.completed ? " completed" : ""}`;
    block.dataset.taskId = task.id;
    block.innerHTML = `<span class="mobile-time">${formatTime(task.start)}–${formatTime(task.start + task.duration)}</span><span class="mobile-event-title"></span><small>${formatHours(task.duration)}</small>`;
    block.querySelector(".mobile-event-title").textContent = task.title;
    list.append(block);
    previousEnd = task.start + task.duration;
  }
  if (previousEnd < 24) list.append(mobileFreeSlot(previousEnd, 24));
  mobilePlanner.append(list);
}

function renderCalendar() {
  calendar.replaceChildren();
  const corner = document.createElement("div");
  corner.className = "time-heading";
  calendar.append(corner);
  for (let day = 0; day < 7; day++) {
    const date = new Date(weekStart);
    date.setDate(date.getDate() + day);
    const heading = document.createElement("div");
    heading.className = "day-heading";
    heading.innerHTML = `<strong>${dayNames[day]}</strong><span>${shortDate(date)}</span>`;
    calendar.append(heading);
  }
  const ruler = document.createElement("div");
  ruler.className = "time-ruler";
  for (let hour = 0; hour < 24; hour += 2) {
    const label = document.createElement("span");
    label.className = "hour-label";
    label.style.top = `${hour * pixelsPerHour}px`;
    label.textContent = formatTime(hour);
    ruler.append(label);
  }
  calendar.append(ruler);
  const today = new Date();
  for (let day = 0; day < 7; day++) {
    const date = new Date(weekStart);
    date.setDate(date.getDate() + day);
    const track = document.createElement("div");
    track.className = "day-track";
    if (date.toDateString() === today.toDateString()) track.classList.add("today");
    const scheduled = tasks.filter(task => task.day === day).sort((a, b) => a.start - b.start);
    let previousEnd = 0;
    for (const task of scheduled) {
      if (task.start > previousEnd) track.append(freeSlot(previousEnd, task.start));
      const block = document.createElement("button");
      block.type = "button";
      block.className = `event ${task.category}${task.duration < 1 ? " compact" : ""}${task.completed ? " completed" : ""}`;
      block.dataset.taskId = task.id;
      block.style.top = `${task.start * pixelsPerHour + 2}px`;
      block.style.height = `${task.duration * pixelsPerHour - 4}px`;
      block.setAttribute("aria-label", `${task.title}, ${task.completed ? "completed, " : ""}${categoryNames[task.category]}, ${dayNames[day]} ${formatTime(task.start)} to ${formatTime(task.start + task.duration)}`);
      const name = document.createElement("strong");
      name.textContent = task.title;
      block.append(name);
      if (task.duration >= 1.5) {
        const time = document.createElement("span");
        time.textContent = `${formatTime(task.start)}–${formatTime(task.start + task.duration)}`;
        block.append(time);
      }
      track.append(block);
      previousEnd = task.start + task.duration;
    }
    if (previousEnd < 24) track.append(freeSlot(previousEnd, 24));
    calendar.append(track);
  }
}

function renderLedger() {
  const hours = categoryHours();
  const bar = document.querySelector("#ledger-bar");
  const rows = document.querySelector("#ledger-rows");
  bar.replaceChildren();
  rows.replaceChildren();
  for (const category of categories) {
    const segment = document.createElement("span");
    segment.className = category;
    segment.style.width = `${hours[category] / 168 * 100}%`;
    bar.append(segment);
    const row = document.createElement("div");
    row.className = "ledger-row";
    row.innerHTML = `<span class="swatch ${category}"></span><span>${categoryNames[category]}</span><strong>${formatHours(hours[category])}</strong>`;
    rows.append(row);
  }
}

function categoryHours() {
  const hours = Object.fromEntries(categories.map(category => [category, 0]));
  for (const task of tasks) if (task.day !== null) hours[task.category] += task.duration;
  hours.free = 168 - categories.slice(0, -1).reduce((sum, category) => sum + hours[category], 0);
  return hours;
}

function renderBacklog() {
  const backlog = tasks.filter(task => task.day === null);
  document.querySelector("#backlog-count").textContent = `(${backlog.length})`;
  const items = document.querySelector("#backlog-items");
  items.replaceChildren();
  if (!backlog.length) {
    const empty = document.createElement("p");
    empty.className = "empty";
    empty.textContent = "Everything has a place this week. Add a task when something comes up.";
    items.append(empty);
  }
  for (const task of backlog) {
    const row = document.createElement("button");
    row.type = "button";
    row.className = `backlog-item${task.completed ? " completed" : ""}`;
    row.dataset.taskId = task.id;
    row.innerHTML = `<span class="swatch ${task.category}"></span><span></span><small>${formatHours(task.duration)}</small>`;
    row.children[1].textContent = task.title;
    row.setAttribute("aria-label", `${task.title}, ${task.completed ? "completed, " : ""}${formatHours(task.duration)}, edit or schedule`);
    items.append(row);
  }
}

function openTask(task, slot) {
  form.reset();
  form.dataset.id = task?.id ?? "";
  form.dataset.originalDay = task?.day === null || !task ? "" : String(task.day);
  document.querySelector("#dialog-title").textContent = task ? "Edit task" : "Add task";
  document.querySelector("#delete-task").hidden = !task;
  document.querySelector("#form-error").hidden = true;
  document.querySelector("#keep-backlog").hidden = true;
  const daySelect = document.querySelector("#task-day");
  daySelect.replaceChildren(new Option("Backlog — schedule later", ""));
  for (let day = 0; day < 7; day++) {
    const date = new Date(weekStart);
    date.setDate(date.getDate() + day);
    daySelect.add(new Option(`${dayNames[day]} ${shortDate(date)}`, String(day)));
  }
  document.querySelector("#task-title").value = task?.title ?? "";
  document.querySelector("#task-category").value = task?.category ?? "focus";
  document.querySelector("#task-duration").value = task?.duration ?? slot?.duration ?? 1;
  document.querySelector("#task-completed").checked = task?.completed ?? false;
  daySelect.value = slot ? String(slot.day) : task?.day === null || !task ? "" : String(task.day);
  document.querySelector("#task-start").value = String(slot?.start ?? task?.start ?? 9);
  updateTimeField();
  dialog.showModal();
  document.querySelector("#task-title").focus();
}

function saveTask(event) {
  event.preventDefault();
  const title = document.querySelector("#task-title").value.trim();
  const category = document.querySelector("#task-category").value;
  const duration = Number(document.querySelector("#task-duration").value);
  const dayValue = document.querySelector("#task-day").value;
  const day = dayValue === "" ? null : Number(dayValue);
  const start = day === null ? null : Number(document.querySelector("#task-start").value);
  const completed = document.querySelector("#task-completed").checked;
  let error = "";
  if (!title) error = "Enter a task name.";
  else if (!Number.isFinite(duration) || duration < 0.5 || duration > 24 || duration * 2 % 1) error = "Choose a duration from 0.5 to 24 hours in half-hour steps.";
  else if (day !== null && start + duration > 24) error = "This task would cross midnight. Choose an earlier start or shorter duration.";
  else if (day !== null) {
    const overlap = tasks.find(task => task.id !== form.dataset.id && task.day === day && start < task.start + task.duration && start + duration > task.start);
    if (overlap) error = `Overlaps ${overlap.title} (${formatTime(overlap.start)}–${formatTime(overlap.start + overlap.duration)}). Choose a free slot.`;
  }
  if (error) {
    const message = document.querySelector("#form-error");
    message.textContent = error;
    message.hidden = false;
    document.querySelector("#keep-backlog").hidden = !error.startsWith("Overlaps") && !error.includes("cross midnight");
    renderSlotSuggestions(true);
    return;
  }
  const task = { id: form.dataset.id || crypto.randomUUID(), title, category, duration, day, start, completed };
  tasks = tasks.filter(item => item.id !== task.id);
  tasks.push(task);
  saveTasks();
  dialog.close();
  render();
}

function updateTimeField() {
  const day = document.querySelector("#task-day").value;
  document.querySelector("#time-field").hidden = day === "";
  if (day === "") document.querySelector("#keep-backlog").hidden = true;
  document.querySelector("#save-task").textContent = day === "" ? form.dataset.id ? "Keep in backlog" : "Add to backlog" : form.dataset.originalDay === "" ? "Schedule task" : "Save changes";
  renderSlotSuggestions();
}

function renderSlotSuggestions(allDays = false) {
  const panel = document.querySelector("#slot-suggestions");
  const duration = Number(document.querySelector("#task-duration").value);
  const dayValue = document.querySelector("#task-day").value;
  const days = allDays || dayValue === "" ? [0, 1, 2, 3, 4, 5, 6] : [Number(dayValue)];
  const slots = days.flatMap(day => availableSlots(day, duration, form.dataset.id));
  panel.replaceChildren();
  panel.hidden = !Number.isFinite(duration) || duration < 0.5 || (dayValue === "" && !form.dataset.id);
  if (panel.hidden) return;
  const heading = document.createElement("strong");
  heading.textContent = allDays || dayValue === "" ? "Open slots this week" : `Open slots on ${dayNames[Number(dayValue)]}`;
  panel.append(heading);
  if (!slots.length) {
    const note = document.createElement("p");
    note.textContent = "No slot fits this duration. Try another day or a shorter task.";
    panel.append(note);
    return;
  }
  for (const slot of slots.slice(0, 3)) {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "suggested-slot";
    button.dataset.slotDay = String(slot.day);
    button.dataset.slotStart = String(slot.start);
    const selected = dayValue === String(slot.day) && document.querySelector("#task-start").value === String(slot.start);
    button.classList.toggle("selected", selected);
    button.setAttribute("aria-pressed", String(selected));
    button.textContent = `${dayNames[slot.day]} ${formatTime(slot.start)}–${formatTime(slot.start + duration)}`;
    panel.append(button);
  }
}

function availableSlots(day, duration, excludedId) {
  const dayTasks = tasks.filter(task => task.day === day && task.id !== excludedId).sort((a, b) => a.start - b.start);
  const slots = [];
  let cursor = 0;
  for (const task of [...dayTasks, { start: 24, duration: 0 }]) {
    if (task.start - cursor >= duration) {
      const daytime = Math.max(cursor, 7);
      const start = daytime + duration <= Math.min(task.start, 22) ? daytime : cursor;
      slots.push({ day, start });
    }
    cursor = Math.max(cursor, task.start + task.duration);
  }
  return slots;
}

function freeSlot(start, end) {
  const slot = document.createElement("div");
  slot.className = "free-slot";
  slot.style.top = `${start * pixelsPerHour + 2}px`;
  slot.style.height = `${(end - start) * pixelsPerHour - 4}px`;
  if (end - start >= 1.5) {
    const label = document.createElement("span");
    label.textContent = `${formatHours(end - start)} free`;
    slot.append(label);
  }
  return slot;
}

function mobileFreeSlot(start, end) {
  const slot = document.createElement("button");
  slot.type = "button";
  slot.className = "mobile-free-slot";
  slot.dataset.freeStart = String(start);
  slot.dataset.freeDuration = String(end - start);
  slot.textContent = `${formatTime(start)}–${formatTime(end)} · ${formatHours(end - start)} available`;
  slot.setAttribute("aria-label", `Add a task in the free slot ${formatTime(start)} to ${formatTime(end)}`);
  return slot;
}

function loadTasks() {
  const saved = localStorage.getItem(storageKey());
  if (saved) {
    try { return JSON.parse(saved); } catch { /* Restore the sample week below. */ }
  }
  return sampleTasks();
}

function saveTasks() {
  localStorage.setItem(storageKey(), JSON.stringify(tasks));
}

function sampleTasks() {
  const list = [];
  const add = (day, start, duration, category, title) => list.push({ id: crypto.randomUUID(), day, start, duration, category, title });
  for (let day = 0; day < 7; day++) {
    add(day, 0, 7, "sleep", "Sleep");
    add(day, 23, 1, "sleep", "Sleep");
    if (day < 5) {
      add(day, 7, 2, "life", "Morning routine");
      add(day, 9, 8, "work", ["Project work", "Team delivery", "Design review", "Build & review", "Wrap up work"][day]);
      add(day, 18, 1, "life", ["Walk", "Groceries", "Gym", "Dinner prep", "Meet a friend"][day]);
      add(day, 19, 3, "focus", ["Write proposal", "Study", "Personal project", "Deep reading", "Plan next steps"][day]);
    }
  }
  add(5, 9, 3, "life", "Family & errands");
  add(5, 13, 2, "focus", "Learn something new");
  add(5, 17, 2, "life", "Dinner with friends");
  add(6, 9, 2, "life", "Home care");
  add(6, 14, 1, "focus", "Review the week");
  add(6, 18, 2, "life", "Family time");
  add(null, null, 2, "focus", "Outline portfolio update");
  add(null, null, 1, "life", "Book dentist appointment");
  add(null, null, 1.5, "work", "Prepare Monday notes");
  return list;
}

function storageKey() { return `168h:${weekStart.getFullYear()}-${weekStart.getMonth() + 1}-${weekStart.getDate()}`; }
function mondayOf(date) { const monday = new Date(date.getFullYear(), date.getMonth(), date.getDate()); monday.setDate(monday.getDate() - (monday.getDay() + 6) % 7); return monday; }
function shortDate(date) { return date.toLocaleDateString("en-US", { month: "short", day: "numeric" }); }
function formatHours(hours) { return `${Number.isInteger(hours) ? hours : hours.toFixed(1)}h`; }
function formatTime(hour) { const h = Math.floor(hour) % 24; return `${String(h).padStart(2, "0")}:${hour % 1 ? "30" : "00"}`; }
