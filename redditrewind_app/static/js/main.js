var currentStep = 1;
var questions = 10;


const nextStepSpans = Array.from(document.querySelectorAll('.next-step'));

if (nextStepSpans.length > 0) {
  const lastNextStepSpan = nextStepSpans[nextStepSpans.length - 1]; // Get the last element
  lastNextStepSpan.style.pointerEvents = 'none'; // Disable clicks
  lastNextStepSpan.style.opacity = '0.5'; // Optional: dim the button to indicate it's disabled
}

// Select all submit buttons
const submitButtons = document.querySelectorAll('button[type="submit"]');

// Disable and set opacity for each submit button
submitButtons.forEach(button => {
  button.style.pointerEvents = 'none'; // Disable interactions
  button.style.opacity = '0.5';       // Set 50% opacity
  button.disabled = true;            // Programmatically disable the button
});

checkCurrentStepAnswer(currentStep)
activateStepCircles()
checkAllCookies()

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

  checkCurrentStepAnswer(currentStep)
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

      }
        currentStep++;
        checkCurrentStepAnswer(currentStep)
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
        
        currentStep--;
        checkCurrentStepAnswer(currentStep)
      } 
    });
    
    // Initial call to update the progress bar
    updateProgressBar();
  } else {
    console.error("Form with ID 'multi-step-form' not found!");
  }
});

document.querySelectorAll('button[type="submit"]').forEach(button => {
  button.addEventListener('click', (event) => {
      // Prevent the default form submission
      event.preventDefault();

      // Perform your custom logic here
      console.log('Done button clicked!');

      // Example: Check if all quizzes are answered
      if (checkAllCookies()) {
          console.log('All quizzes answered. Proceeding...');
            // Collect form data (if needed)
      const formData = $('#multi-step-form').serialize(); // This will collect the form data

      // Submit the data via AJAX
      $.ajax({
        url: '/submit_choices', // The URL where you want to send the data
        type: 'POST',
        data: formData, // Send the form data
        dataType: 'json', // Ensure we get the response in JSON format
        success: function(response) {
            console.log(response);  // Log the response to debug
            window.location.href = '/finished'
        },
        error: function(xhr, status, error) {
            // Handle AJAX errors (e.g., network issues)
            console.error('Error occurred: ', error);
            alert('An error occurred. Please try again.');
        }
    });
      } else {
          console.error('Not all quizzes are answered.');
          alert('Please answer all quizzes before submitting.');
      }
  });
});

document.querySelectorAll('input[name="choice"]').forEach(choice => {
  choice.addEventListener('click', (event) => {
    const selectedChoice = event.target; // The clicked radio button
    const quizId = selectedChoice.closest('[quiz-id]').getAttribute('quiz-id'); // Get the quiz ID from the parent container
    const choiceId = selectedChoice.value; // Get the value of the selected choice

    // Set a cookie with the quiz ID and choice ID
    document.cookie = `quiz_${quizId}=${choiceId}; path=/; max-age=3600`; // Cookie expires in 1 hour

    console.log(`Saved cookie: quiz_${quizId}=${choiceId}`);

    checkAllCookies();
  });
});

// Function to check if all cookies for all quizzes are set
function checkAllCookies() {
  // Get all quiz IDs from the DOM
  const quizIds = Array.from(document.querySelectorAll('[quiz-id]')).map(
    element => element.getAttribute('quiz-id')
  );

  // Check cookies for each quiz ID
  const missingQuizIds = quizIds.filter(quizId => {
    return !document.cookie.includes(`quiz_${quizId}=`);
  });
  activateStepCircles();

  if (missingQuizIds.length === 0) {
    console.log('All quizzes are answered!');
    // Select all submit buttons
    const submitButtons = document.querySelectorAll('button[type="submit"]');

    // Disable and set opacity for each submit button
    submitButtons.forEach(button => {
    button.style.pointerEvents = 'auto'; // Enable interactions
    button.style.opacity = '1';       // Set Full opacity
    button.disabled = false;            
    button.textContent = `Done (${questions-missingQuizIds}/${questions})`;    
    });
    return true
  } else {
    console.log('Not all quizzes are answered. Missing quiz IDs:', missingQuizIds);
    // Optionally disable a "Submit" button

    const submitButtons = document.querySelectorAll('button[type="submit"]');

    // Disable and set opacity for each submit button
    submitButtons.forEach(button => {
      button.textContent = `Done (${questions - missingQuizIds.length}/${questions})`;  
  });
  
 }
}


function updateCurrentStepUI() {
  // Get all step-circle elements
  const stepCircles = document.querySelectorAll('.step-circle');
  
  // Loop through all step circles and apply/remove the "active" class
  stepCircles.forEach((circle, index) => {
    if (index + 1 === currentStep) {
      circle.classList.add('answered'); // Add active class to the current step
    } 
  });
}

function activateStepCircles() {
  // Parse cookies into an object
  const cookies = document.cookie.split("; ").reduce((acc, cookie) => {
    const [key, value] = cookie.split("=");
    acc[key] = value;
    return acc;
  }, {});

  // Find all step circles
  const stepCircles = document.querySelectorAll(".step-circle");

  stepCircles.forEach((circle, index) => {
    // Step numbers are 1-based, so add 1 to the index
    const stepNumber = index + 1;

    // Get the quiz ID for this step
    const quizElement = document.querySelector(`.step.step-${stepNumber} [quiz-id]`);

    if (quizElement) {
      const quizId = quizElement.getAttribute("quiz-id");

      // Check if there's a stored answer in cookies for this quiz ID
      if (cookies[`quiz_${quizId}`]) {
        // Activate the circle if an answer is stored
        circle.style.backgroundColor = "#FF5700"; // Example active background color
        circle.style.color = "#fff"; // Example active text color
      } else {
        // Reset the circle to default if no answer is stored
        circle.style.backgroundColor = "#fff"; // Default background color
        circle.style.color = "#FF5700"; // Default text color
      }
    } else {
      console.warn(`No quiz element found for step ${stepNumber}`);
    }
  });
}

function checkCurrentStepAnswer(currentStep) {
  // Find the quiz container for the current step
  const currentQuizElement = document.querySelector(`.step.step-${currentStep} [quiz-id]`);
  
  if (!currentQuizElement) {
    console.warn(`No quiz found for step ${currentStep}`);
    return;
  }

  // Get the quiz ID from the 'quiz-id' attribute
  const quizId = currentQuizElement.getAttribute('quiz-id');

  // Parse cookies into an object
  const cookies = document.cookie.split("; ").reduce((acc, cookie) => {
    const [key, value] = cookie.split("=");
    acc[key] = value;
    return acc;
  }, {});

  // Check if there's a stored answer for this quiz ID
  if (cookies[`quiz_${quizId}`]) {
    const choiceId = cookies[`quiz_${quizId}`]; // Get the choice ID from the cookie

    // Find the radio button corresponding to this choice
    const choiceInput = document.querySelector(`.step.step-${currentStep} input[type="radio"][id="${choiceId}"]`);

    if (choiceInput) {
      choiceInput.checked = true; // Check the radio button
      console.log(`Choice ${choiceId} for Quiz ${quizId} has been selected.`);
    } else {
      console.warn(`No input found for choice ID ${choiceId} of Quiz ${quizId}.`);
    }
  } else {
    console.log(`No answer stored in cookies for Quiz ${quizId}.`);
  }
}

document.getElementById('submit-guess').addEventListener('click', function () {
  const userGuess = document.getElementById('guess-input').value.toLowerCase().trim();
  const answers = document.querySelectorAll('.hidden-answer');

  answers.forEach(answer => {
      if (answer.textContent.toLowerCase() === userGuess) {
          answer.style.visibility = 'visible'; // Reveal correct answer
      }
  });

  document.getElementById('guess-input').value = ''; // Clear input
});





