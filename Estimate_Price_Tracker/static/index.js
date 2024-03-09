function init() {
  // Function to open the signup modal
  function openSignupModal() {
    var modal = new bootstrap.Modal(
      document.getElementById("modalRegisterForm")
    );
    modal.show();
  }
  // Function to open the update modal
  function openUpdateModal() {
    var modal = new bootstrap.Modal(document.getElementById("modalUpdateForm"));
    modal.show();
  }

  // Define the function to navigate to the user's home page
  function goToUserHomePage() {
    console.log("Button clicked!"); // For testing purposes
    // Redirect to the user's home page
    window.location.href = "/user-home"; // Replace with the actual URL for the user's home page
  }

  // Get the button and attach a click event listener
  var backButton = document.getElementById("backButton");
  if (backButton) {
    backButton.addEventListener("click", goToUserHomePage);
  } else {
    console.error("Back button element not found.");
  }

  // Function to open the login modal
  function openLoginModal() {
    var modal = new bootstrap.Modal(document.getElementById("modalLoginForm"));
    modal.show();
  }

  var logoutButton = document.getElementById("logoutBtn");
  if (logoutButton) {
    logoutButton.addEventListener("click", function () {
      // Perform the logout action here, e.g., by redirecting to a logout endpoint
      window.location.href = "/logout";
    });
  }

  // Attach click event listeners to the signup and login links
  var signUpLink = document.getElementById("signUpLink");
  var loginLink = document.getElementById("loginLink");
  var updateLink = document.getElementById("updateLink");

  if (signUpLink) {
    signUpLink.addEventListener("click", openSignupModal);
  }

  if (loginLink) {
    loginLink.addEventListener("click", openLoginModal);
  }
  if (updateLink) {
    updateLink.addEventListener("click", openUpdateModal);
  }

  const connectUsEmailLink = document.getElementById("connectUsEmailLink");

  connectUsEmailLink.addEventListener("click", (event) => {
    event.preventDefault(); // Prevent the default link behavior

    // Open the email dialog
    window.location.href = "mailto:connect@estimateit.com";
  });

  // Function to register a new user
  function registerUser() {
    var username = document.getElementById("orangeForm-username").value;
    var first_name = document.getElementById("orangeForm-firstname").value;
    var last_name = document.getElementById("orangeForm-lastname").value;
    var email = document.getElementById("orangeForm-email").value;
    var password = document.getElementById("orangeForm-pass").value;

    var data = {
      username: username,
      first_name: first_name,
      last_name: last_name,
      email: email,
      password: password,
    };

    fetch("/register", {
      method: "POST",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.text())
      .then((data) => {
        console.log(data);
        var registrationResponse = document.getElementById(
          "registrationResponse"
        );
        if (registrationResponse) {
          registrationResponse.innerHTML = data;
        }

        if (data.includes("successful")) {
          window.location.href = "/user-home"; // Adjust the URL as needed
        }
      });
  }

  // Function to update user-info
  function update_user() {
    var username = document.getElementById("orangeForm-username").value;
    var first_name = document.getElementById("orangeForm-firstname").value;
    var last_name = document.getElementById("orangeForm-lastname").value;
    var data = {
      username: username,
      first_name: first_name,
      last_name: last_name,
    };

    fetch("/update_user", {
      method: "POST",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.text())
      .then((data) => {
        console.log(data);
        var updationResponse = document.getElementById("updationResponse");
        if (updationResponse) {
          updationResponse.innerHTML = data;
        }

        if (data.includes("successful")) {
          window.location.href = "/user_profile"; // Adjust the URL as needed
        }
      });
  }

  // Function to log in a user
  function loginUser() {
    var email = document.getElementById("orangeForm-email").value;
    var password = document.getElementById("orangeForm-pass").value;

    var data = {
      email: email,
      password: password,
    };

    fetch("/login", {
      method: "POST",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => response.text())
      .then((data) => {
        console.log(data);
        var loginResponse = document.getElementById("loginResponse");
        if (loginResponse) {
          loginResponse.innerHTML = data;
        }

        if (data.includes("successful")) {
          window.location.href = "/user-home"; // Adjust the URL as needed
        }
      });
  }

  // Attach click event listeners to the signup and login buttons
  var signupButton = document.getElementById("signupButton");
  var loginButton = document.getElementById("loginButton");
  var updateButton = document.getElementById("updateButton");

  if (signupButton) {
    signupButton.addEventListener("click", registerUser);
  }

  if (loginButton) {
    loginButton.addEventListener("click", loginUser);
  }
  if (updateButton) {
    updateButton.addEventListener("click", update_user);
  }
}

function readmore() {
  var dots = document.getElementById("dots");
  var moreText = document.getElementById("more");
  var btnText = document.getElementById("readmore-btn");

  if (dots.style.display === "none") {
    dots.style.display = "inline";
    btnText.innerHTML = "Read more...";
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    btnText.innerHTML = "Read less";
    moreText.style.display = "inline";
  }
}

document.addEventListener("DOMContentLoaded", init);
