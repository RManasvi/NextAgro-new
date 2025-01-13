// body {
//     font-family: Arial, sans-serif;
//     margin: 0;
//     padding: 0;
//     display: flex;
//     justify-content: center;
//     align-items: center;
//     min-height: 100vh;
//     background: linear-gradient(to right, #a8e063, #56ab2f);
// }

// .container {
//     background-color: white;
//     padding: 2rem;
//     border-radius: 10px;
//     box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
//     width: 100%;
//     max-width: 400px;
// }

// h1 {
//     text-align: center;
//     color: #56ab2f;
//     margin-bottom: 1rem;
// }

// .tabs {
//     display: flex;
//     justify-content: center;
//     margin-bottom: 1rem;
// }

// .tab {
//     background-color: #f0f0f0;
//     border: none;
//     padding: 0.5rem 1rem;
//     margin: 0 0.5rem;
//     cursor: pointer;
//     border-radius: 5px;
//     transition: background-color 0.3s;
// }

// .tab.active {
//     background-color: #56ab2f;
//     color: white;
// }

// form {
//     display: none;
// }

// form.active {
//     display: flex;
//     flex-direction: column;
// }

// input {
//     margin-bottom: 1rem;
//     padding: 0.5rem;
//     border: 1px solid #ccc;
//     border-radius: 5px;
// }

// button {
//     background-color: #56ab2f;
//     color: white;
//     border: none;
//     padding: 0.5rem;
//     border-radius: 5px;
//     cursor: pointer;
//     transition: background-color 0.3s;
// }

// button:hover {
//     background-color: #4a9428;
// }

const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});
  