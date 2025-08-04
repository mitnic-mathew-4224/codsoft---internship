const display = document.getElementById('display');
const buttons = document.querySelectorAll('.btn');
const clearBtn = document.getElementById('clear');
const equalsBtn = document.getElementById('equals');

let input = "";

buttons.forEach(button => {
  const value = button.getAttribute('data-value');

  if (value) {
    button.addEventListener('click', () => {
      input += value;
      display.textContent = input;
    });
  }
});

clearBtn.addEventListener('click', () => {
  input = "";
  display.textContent = "0";
});

equalsBtn.addEventListener('click', () => {
  try {
    const result = eval(input);
    display.textContent = result;
    input = result.toString(); // Allows chaining
  } catch (error) {
    display.textContent = "Error";
    input = "";
  }
});

