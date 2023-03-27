const measurementsContainer = document.querySelector("#measurements");

const measurementList = [
  "cl",
  "cup",
  "dkg",
  "dl",
  "fl",
  "g",
  "gal",
  "kg",
  "l",
  "large",
  "lb",
  "medium",
  "mg",
  "ml",
  "oz",
  "package",
  "pt",
  "qt",
  "small",
  "t",
  "tbs",
  "tsp",
];

const inputContainerClassList = [
  "grid",
  "gap-2",
  "grid-cols-[auto_7rem_5rem_3rem]",
  "mt-4",
];

const inputClassList = [
  "bg-gray-50",
  "border",
  "border-gray-300",
  "text-gray-900",
  "text-sm",
  "rounded-lg",
  "focus:ring-blue-500",
  "focus:border-blue-500",
  "block",
  "w-full",
  "p-2.5",
  "dark:bg-gray-700",
  "dark:border-gray-600",
  "dark:placeholder-gray-400",
  "dark:text-white",
  "dark:focus:ring-blue-500",
  "dark:focus:border-blue-500",
];

const btnClassList = [
  "text-white",
  "bg-gray-800",
  "hover:bg-gray-900",
  "focus:outline-none",
  "focus:ring-4",
  "focus:ring-gray-300",
  "font-medium",
  "rounded-lg",
  "text-sm",
  "px-5",
  "py-2.5",
  "dark:bg-gray-800",
  "dark:hover:bg-gray-700",
  "dark:focus:ring-gray-700",
  "dark:border-gray-700",
  "w-full",
];

function createEl(tag) {
  return document.createElement(tag);
}

function createIngredientInput() {
  const input = createEl("input");
  input.type = "text";
  inputClassList.forEach(function (className) {
    input.classList.add(className);
  });
  input.name = "ingredient";
  input.placeholder = "Ingredient";

  return input;
}

function createAmountInput() {
  const input = createEl("input");
  input.type = "number";
  input.min = 0.1;
  input.step = 0.1;
  input.value = 1;
  inputClassList.forEach(function (className) {
    input.classList.add(className);
  });
  input.name = "amount";
  input.placeholder = "Amount";

  return input;
}

function createMeasurementInput() {
  const select = createEl("select");
  select.name = "measurement";
  inputClassList.forEach(function (className) {
    select.classList.add(className);
  });

  measurementList.forEach(function (measurement) {
    const option = createEl("option");
    option.innerText = measurement;
    option.value = measurement;

    select.appendChild(option);
  });

  return select;
}

function addInputGroup() {
  const container = createEl("div");
  inputContainerClassList.forEach(function (className) {
    container.classList.add(className);
  });

  const ingredient = createIngredientInput();
  const amount = createAmountInput();
  const measurement = createMeasurementInput();

  const removeBtn = createEl("button");
  btnClassList.forEach(function (className) {
    removeBtn.classList.add(className);
  });
  removeBtn.innerText = "X";
  removeBtn.type = "button";
  removeBtn.addEventListener("click", function () {
    container.remove();
  });

  container.appendChild(ingredient);
  container.appendChild(amount);
  container.appendChild(measurement);
  container.appendChild(removeBtn);

  measurementsContainer.appendChild(container);
}

function handleOnRemoveBtnClick(event) {
  event.target.parentElement.remove();
}

function handleOnAddBtnClick() {
  addInputGroup();
}
