const candle = document.querySelector(".candle");
candle.addEventListener("click", () => {
  candle.textContent = "💨"; // blown-out effect
  alert("🎉 Your message has been sent! Time to celebrate!"); // optional popup
});
document.addEventListener("DOMContentLoaded", function () {
  const navbar = document.querySelector(".navbar");
  if (navbar) {
    document.body.style.paddingTop = navbar.offsetHeight + "px";
  }
});
document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener("click", function (e) {
    e.preventDefault();
    document
      .querySelector(this.getAttribute("href"))
      .scrollIntoView({ behavior: "smooth" });
  });
});
window.addEventListener("load", function () {
  document.querySelectorAll("img").forEach((img) => {
    img.style.height = "auto";
  });
});
window.addEventListener("resize", function () {
  document.querySelectorAll("img").forEach((img) => {
    img.style.height = "auto";
  });
});

const contactForm = document.querySelector("#contactForm");

if (contactForm) {
  contactForm.addEventListener("submit", function () {
    const btn = contactForm.querySelector("button");
    btn.disabled = true;
    btn.innerText = "Sending...";
  });
}

function adjustPadding() {
  const nav = document.querySelector(".navbar");
  document.body.style.paddingTop = nav.offsetHeight + "px";
}

window.addEventListener("load", adjustPadding);
window.addEventListener("resize", adjustPadding);
