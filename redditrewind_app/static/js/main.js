var currentStep = 1;
var questions = 10;

function displayStep(stepNumber) {
  if (stepNumber >= 1 && stepNumber <= questions) {
    $(".step-" + currentStep).hide();
    $(".step-" + stepNumber).show();
    currentStep = stepNumber;
    updateProgressBar();
  }
}

// Define the updateProgressBar function
var updateProgressBar = function() {
  var progressPercentage = ((currentStep - 1) / 9) * 10* questions;
  console.log("currentStep:", currentStep);
  console.log("Step Circle:", $(".step-" + currentStep).find(".step-circle"));
  $(".progress-bar").css("width", progressPercentage + "%");
  $(".step-" + currentStep).find(".step-circle").css({
    "background-color": "#FF5700",
    "border": "2px solid #FFF",
    "color": "#FFF"
});
};

$(document).ready(function() {
  // Check if the multi-step form exists
  if ($('#multi-step-form').length) {
    // Initially hide all steps except the first one
    $(".step").slice(1).hide()

    $(".next-step").click(function() {
      if (currentStep < questions) {
        // Apply fade out animation and wait for it to complete
        $(".step-" + currentStep).addClass("animate__animated animate__fadeOutLeft");
        
        // Increase the step number
        

        // After the fade-out animation completes (500ms), change the step
        setTimeout(function() {
          $(".step").removeClass("animate__animated animate__fadeOutLeft").hide(); // Hide all steps
          $(".step-" + currentStep).show().addClass("animate__animated animate__fadeInRight"); // Show the next step with fadeInRight animation
          updateProgressBar(); // Update the progress bar after the step transition
        }, 500); // Make sure this matches the duration of the fadeOut animation

        const form = $("#multi-step-form")[0];
        var quizId = $(".step-" + currentStep).find("[quiz-id]").attr("quiz-id");
      
      
        console.log('No choice selected.');
        // Check if a choice is selected
        const selectedChoice = form.querySelector('input[name="choice"]:checked');
        if (selectedChoice) {
          const choiceId = selectedChoice.value; // Get the selected choice ID
          console.log(' choice selected.');
          // Set the cookie with both quizId and choiceId
          document.cookie = `quiz_${quizId}=${choiceId}; path=/; max-age=3600`; // Cookie will expire in 1 hour
        } else {
          console.log('No choice selected.');
        }
        currentStep++;
        selectedChoice.checked = false;
      }
    });

    $(".prev-step").click(function() {
      if (currentStep > 1) {
        // Apply fade out animation for previous step
        $(".step-" + currentStep).addClass("animate__animated animate__fadeOutRight");
        

        // After the fade-out animation completes (500ms), change the step
        setTimeout(function() {
          $(".step").removeClass("animate__animated animate__fadeOutRight").hide(); // Hide all steps
          $(".step-" + currentStep).show().addClass("animate__animated animate__fadeInLeft"); // Show the previous step with fadeInLeft animation
          updateProgressBar(); // Update the progress bar after the step transition
        }, 500); // Make sure this matches the duration of the fadeOut animation

        const form = $("#multi-step-form")[0];
        var quizId = $(".step-" + currentStep).find("[quiz-id]").attr("quiz-id");
      
      
        console.log('No choice selected.');
        // Check if a choice is selected
        const selectedChoice = form.querySelector('input[name="choice"]:checked');
        if (selectedChoice) {
          const choiceId = selectedChoice.value; // Get the selected choice ID
          console.log(' choice selected.');
          // Set the cookie with both quizId and choiceId
          document.cookie = `quiz_${quizId}=${choiceId}; path=/; max-age=3600`; // Cookie will expire in 1 hour
        } else {
          console.log('No choice selected.');
        }
        currentStep--;
        selectedChoice.checked = false;
      } 
    });
    
    $(".submit").click(function() {
      if (currentStep = questions){
        
        // Collect form data (if needed)
      const formData = $('#multi-step-form').serialize(); // This will collect the form data

      // Submit the data via AJAX
      $.ajax({
        url: '/submit_choices', // The URL where you want to send the data
        type: 'POST',
        data: formData, // Send the form data
        success: function(response) {
          // If the server responds successfully, redirect to the "finished" page
          if (response.success) {
            window.location.href = 'finished.html'; // Redirect to finished page
          } else {
            // Handle errors (if any)
            alert('Something went wrong. Please try again.');
          }
        },
        error: function(xhr, status, error) {
          // Handle AJAX errors (e.g., network issues)
          console.error('Error occurred: ', error);
          alert('An error occurred. Please try again.');
        }
      });
    }

    });
    // Initial call to update the progress bar
    updateProgressBar();
  } else {
    console.error("Form with ID 'multi-step-form' not found!");
  }
});


// Wait for the DOM to be fully loaded before adding event listeners
document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('form'); // Ensure you select the correct form
  const saveNextButton = document.querySelector(".step-" + currentStep + " .next-step");

  if (!saveNextButton) {
      console.error("Save & Next button not found for current step.");
      return;
  }

  // Add an event listener to check for changes in the form (both selection and deselection)
  form.addEventListener('change', () => {
      // Find the selected choice (checked radio button)
      const selectedChoice = form.querySelector('input[name="choice"]:checked');

      // Update the button text based on whether a choice is selected or not
      if (selectedChoice) {
          console.log("Choice was selected");
          saveNextButton.textContent = "Save & Next"; // Change to "Save & Next" if a choice is selected
      } else {
          console.log("Choice was not selected");
          saveNextButton.textContent = "Next"; // Change back to "Next" if no choice is selected
      }
  });
});

document.addEventListener('DOMContentLoaded', () => {
  const radioButtons = document.querySelectorAll('input[type="radio"][name="choice"]');
  let lastChecked = null; // Keep track of the last checked radio button

  radioButtons.forEach(radio => {
      radio.addEventListener('click', function () {
          if (this === lastChecked) {
              this.checked = false; // Uncheck the radio button
              lastChecked = null;  // Reset the last checked button
          } else {
              lastChecked = this; // Update the last checked button
          }
      });
  });
});

