var currentStep = 1;

// Define the updateProgressBar function
var updateProgressBar = function() {
  var progressPercentage = ((currentStep - 1) / 9) * 100;
  $(".progress-bar").css("width", progressPercentage + "%");
};

$(document).ready(function() {
  // Check if the multi-step form exists
  if ($('#multi-step-form').length) {
    // Initially hide all steps except the first one
    $(".step").slice(1).hide()

    $(".next-step").click(function() {
      if (currentStep < 10) {
        // Apply fade out animation and wait for it to complete
        $(".step-" + currentStep).addClass("animate__animated animate__fadeOutLeft");
        
        // Increase the step number
        currentStep++;

        // After the fade-out animation completes (500ms), change the step
        setTimeout(function() {
          $(".step").removeClass("animate__animated animate__fadeOutLeft").hide(); // Hide all steps
          $(".step-" + currentStep).show().addClass("animate__animated animate__fadeInRight"); // Show the next step with fadeInRight animation
          updateProgressBar(); // Update the progress bar after the step transition
        }, 500); // Make sure this matches the duration of the fadeOut animation
      } else if (currentStep = 10){
        
        window.location.href = 'finished';

      }
    });

    $(".prev-step").click(function() {
      if (currentStep > 1) {
        // Apply fade out animation for previous step
        $(".step-" + currentStep).addClass("animate__animated animate__fadeOutRight");
        
        // Decrease the step number
        currentStep--;

        // After the fade-out animation completes (500ms), change the step
        setTimeout(function() {
          $(".step").removeClass("animate__animated animate__fadeOutRight").hide(); // Hide all steps
          $(".step-" + currentStep).show().addClass("animate__animated animate__fadeInLeft"); // Show the previous step with fadeInLeft animation
          updateProgressBar(); // Update the progress bar after the step transition
        }, 500); // Make sure this matches the duration of the fadeOut animation
      } 
    });

    // Initial call to update the progress bar
    updateProgressBar();
  } else {
    console.error("Form with ID 'multi-step-form' not found!");
  }
});

document.addEventListener('submit', function (event) {
  event.preventDefault();
  
  // Extract data from the form
  const form = event.target;
  const submitButton = form.querySelector('.next-step'); // Get the submit button
    
  const quizId = submitButton.getAttribute('data-quiz-id');  // Get the quiz ID (make sure it's in the form element as a data attribute)
  
  // Check if a choice is selected
  const selectedChoice = form.querySelector('input[name="choice"]:checked');
  if (selectedChoice) {
    const choiceId = selectedChoice.value; // Get the selected choice ID
    
    // Create a cookie name based on both quizId and choiceId
    const cookieName = `quiz_${quizId}_choice_${choiceId}`;
    
    // Set the cookie with both quizId and choiceId
    document.cookie = `quiz_${quizId}=${choiceId}; path=/; max-age=3600`; // Cookie will expire in 1 hour
    
    // Optionally, log the cookie to check if it's set
    console.log(`Cookie set: ${quizId}=${choiceId}`);
  } else {
    console.log('No choice selected.');
  }

  // Log the cookie to confirm it's set
  console.log('Cookie set:', document.cookie);
  
  const formData = new FormData(form); // Form data including CSRF token and user c
});
