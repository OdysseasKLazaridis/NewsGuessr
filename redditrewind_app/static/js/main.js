var currentStep = 1;
var questions = 10;


const nextStepSpans = Array.from(document.querySelectorAll('.next-step'));

if (nextStepSpans.length > 0) {
  const lastNextStepSpan = nextStepSpans[nextStepSpans.length - 1]; // Get the last element
  lastNextStepSpan.style.pointerEvents = 'none'; // Disable clicks
  lastNextStepSpan.style.opacity = '0.5'; // Optional: dim the button to indicate it's disabled
}


const firstPrevStepSpans = Array.from(document.querySelectorAll('.prev-step'));

// Check if there are any .prev-step elements
if (firstPrevStepSpans.length > 0) {
  const firstPrevStepSpan = firstPrevStepSpans[0]; // Access the first element
  firstPrevStepSpan.style.pointerEvents = 'none'; // Disable clicks
  firstPrevStepSpan.style.opacity = '0.5'; // Optional: dim the button to indicate it's disabled
}


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
        
        // After the fade-out animation completes (500ms), change the step
        setTimeout(function() {
          $(".step").removeClass("animate__animated animate__fadeOutLeft").hide(); // Hide all steps
          $(".step-" + currentStep).show().addClass("animate__animated animate__fadeInRight"); // Show the next step with fadeInRight animation
          updateProgressBar(); // Update the progress bar after the step transition
        }, 500); // Make sure this matches the duration of the fadeOut animation

        const form = $("#multi-step-form")[0];
        var quizId = $(".step-" + currentStep).find("[quiz-id]").attr("quiz-id");
    
        // Check if a choice is selected
        const selectedChoice = form.querySelector('input[name="choice"]:checked');
        console.log(selectedChoice)
          if (selectedChoice) {
            const choiceId = selectedChoice.value; // Get the selected choice ID
          
            // Set the cookie with both quizId and choiceId
            document.cookie = `quiz_${quizId}=${choiceId}; path=/; max-age=3600`; // Cookie will expire in 1 hour
            selectedChoice.checked = false; 
          } else {
            console.log('No choice selected.');
          }

        
        } else {
          console.log('No choice selected.');
        }
        currentStep++;
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
      
      
        // Check if a choice is selected
        const selectedChoice = form.querySelector('input[name="choice"]:checked');
        if (selectedChoice) {
          const choiceId = selectedChoice.value; // Get the selected choice ID
          // Set the cookie with both quizId and choiceId
          document.cookie = `quiz_${quizId}=${choiceId}; path=/; max-age=3600`; // Cookie will expire in 1 hour
          selectedChoice.checked = false;  // Only uncheck if the element is found
        } else {
          console.log('No choice selected.');
        }
        currentStep--;
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




