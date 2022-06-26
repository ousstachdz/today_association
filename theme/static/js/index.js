const body = document.getElementById("main");
function switch_theme() {
  if (body.classList.contains("dark")) {
    body.classList.remove("dark");
  } else {
    body.classList.add("dark");
  }
}

let bg_about = document.getElementById("bg_about");
console.log(bg_about);

function changing_about_bg() {
  bg_about.style.backgroundImage = `url('static/assets/hero3.jpg')`;
  setInterval(() => {
    let number = Math.floor(Math.random() * 6);
    bg_about.style.backgroundImage = `url('static/assets/hero${number}.jpg')`;
  }, 3000);
}
changing_about_bg();
