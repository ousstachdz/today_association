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
const preview = document.getElementById("preview_img");
if (img != null) {
  img.onchange = (evt) => {
    const [file] = img.files;
    if (file) {
      preview.src = URL.createObjectURL(file);
    }
  };
}

const type = document.getElementById("type");
if (type != null) {
  type.onchange = (evt) => {
    console.log(evt.target.value);
    const price = document.getElementById("price");
    const enddate = document.getElementById("enddate");

    if (evt.target.value == "Post") {
      price.classList.add("hidden");
      enddate.classList.add("hidden");
    }
    if (evt.target.value == "Trip") {
      price.classList.remove("hidden");
      enddate.classList.add("hidden");
    }
    if (evt.target.value == "Event") {
      price.classList.add("hidden");
      enddate.classList.remove("hidden");
    }
  };
}
