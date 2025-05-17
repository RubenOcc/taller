document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("client_register_form");

  if (form) {
    form.addEventListener("submit", async function (e) {
      e.preventDefault(); // Prevent page reload

      const formData = new FormData(this);
      const data = Object.fromEntries(formData.entries());
    
      console.log("Form data:", data);
      const response = await fetch("/client/register", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      const result = await response.json();
      if (response.ok) {
        alert(result.message); // Client successfully registered
        this.reset(); // Optional: reset form after success
        $('#clients').DataTable().ajax.reload();
      } else {
        alert("Error: " + result.message);
      }
    });
  } else {
    console.error("❌ Form with ID 'clients_register_form' not found.");
  }
});
