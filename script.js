function checkNews() {
  const text = document.getElementById("newsInput").value;

  fetch("/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text: text })
  })
  .then(response => response.json())
  .then(data => {
    document.getElementById("result").innerText = data.prediction;

    // Change text color based on prediction
    if (data.prediction.includes("TRUE")) {
      document.getElementById("result").style.color = "green";
    } else if (data.prediction.includes("FAKE")) {
      document.getElementById("result").style.color = "red";
    } else {
      document.getElementById("result").style.color = "black";
    }
  })
  .catch(error => console.error("Error:", error));
}

function resetForm() {
  document.getElementById("newsInput").value = "";
  document.getElementById("result").innerText = "";
}