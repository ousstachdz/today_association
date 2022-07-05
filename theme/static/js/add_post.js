const title = document.getElementById("title");
if (title != null) {
  title.onchange = (evt) => {
    const d_title = document.getElementById("d-title");
    d_title.innerHTML = evt.target.value;
  };
}
const date = document.getElementById("date");
if (date != null) {
  date.onchange = (evt) => {
    console.log(evt.target.value);
  };
}

const content = document.getElementById("content");
if (content != null) {
  content.onchange = (evt) => {
    console.log(evt.target.value);
  };
}
const price = document.getElementById("price");
if (price != null) {
  price.onchange = (evt) => {
    console.log(evt.target.value);
  };
}
const enddate = document.getElementById("enddate");
if (enddate != null) {
  enddate.onchange = (evt) => {
    console.log(evt.target.value);
  };
}
