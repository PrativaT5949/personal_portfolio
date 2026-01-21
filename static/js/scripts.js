const candle = document.querySelector(".candle");
candle.addEventListener("click", () => {
  candle.textContent = "💨"; // blown-out effect
  alert("🎉 Your message has been sent! Time to celebrate!"); // optional popup
});
