let img = [
  "https://cdn-icons-png.flaticon.com/128/7268/7268615.png",
  "https://cdn-icons-png.flaticon.com/128/455/455691.png",
  "https://cdn-icons-png.flaticon.com/128/154/154843.png",
  "https://cdn-icons-png.flaticon.com/128/16036/16036591.png",
  "https://cdn-icons-png.flaticon.com/128/1017/1017466.png",
  "https://cdn-icons-png.flaticon.com/128/17102/17102771.png",
  "https://cdn-icons-png.flaticon.com/128/11067/11067898.png",
  "https://cdn-icons-png.flaticon.com/128/7710/7710466.png",
  "https://cdn-icons-png.flaticon.com/128/18645/18645929.png"
];

let titles = [
  "Один",
  "Два",
  "Три",
  "Четыре",
  "Пять",
  "вапоравпротлвап",
  "СЕМЬЬЬ",
  "Вовчсмрмтлывпмжтьывапиьаыврилаврпьэиав ауопавь  аврпавлдржэпиьра",
  "9"
];

class Block {
  constructor(img, h2) {
    this.src = img;
    this.h2 = h2;
  }

  render() {
    for (let i = 0; i < this.src.length; i++) {
      let out = `
        <img src="${this.src[i]}" alt="">
        <h2>${this.h2[i]}</h2>
      `;
      document.querySelector(`#block${i + 1}`).innerHTML = out;
    }
  }
}

let blocks = new Block(img, titles);
blocks.render();