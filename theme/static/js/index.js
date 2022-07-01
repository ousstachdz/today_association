// const body = document.getElementById("main");
// function switch_theme() {
//   if (body.classList.contains("dark")) {
//     body.classList.remove("dark");
//   } else {
//     body.classList.add("dark");
//   }
// }

function changing_about_bg() {
  let bg_about = document.getElementById("bg_about");
  if (bg_about) {
    bg_about.style.backgroundImage = `url('static/assets/hero3.jpg')`;
    setInterval(() => {
      let number = Math.floor(Math.random() * 6);
      bg_about.style.backgroundImage = `url('static/assets/hero${number}.jpg')`;
    }, 3000);
  }
}
changing_about_bg();

const img = document.getElementById("img");
const avatar = document.getElementById("avatar_img");
img.onchange = (evt) => {
  const [file] = img.files;
  if (file) {
    avatar.src = URL.createObjectURL(file);
  }
};
