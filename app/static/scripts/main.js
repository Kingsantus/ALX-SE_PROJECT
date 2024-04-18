// start conversation 

document.querySelectorAll('.conversation-item-dropdown-toggle').forEach(function(item) {
    item.addEventListener('click', function(e) {
        e.preventDefault();
        if(this.parentElement.classList.contains('active')) {
            this.parentElement.classList.remove('active');
        } else {
            document.querySelectorAll('.conversation-item-dropdown').forEach(function(i) {
                i.classList.remove('active');
            });
            this.parentElement.classList.add('active');
        }
    });
});

document.addEventListener('click', function(e) {
    if(!e.target.matchs('.conversation-item-dropdown, .conversation-item-dropdown *')) {
        document.querySelectorAll('.conversation-item-dropdown').forEach(function(i) {
            i.classList.remove('active')
        })
    }
})

document.querySelectorAll('.conversation-form-input').forEach(function(item) {
    item.addEventListener('input', function() {
        this.rows = this.value.split('\n').length
    })
})

document.querySelectorAll('[data-conversation]').forEach(function(item) {
    item.addEventListener('click', function(e) {
        e.preventDefault()
        document.querySelectorAll('.conversation').forEach(function(i) {
            i.classList.remove('active')
        })
        document.querySelector(this.dataset.conversation).classList.add('active')
    })
})

document.querySelectorAll('.conversation-back').forEach(function(item) {
    item.addEventListener('click', function(e) {
        e.preventDefault()
        this.closest('.conversation').classList.remove('active')
        document.querySelector('.conversation-default').classList.add('active')
    })
})

document.addEventListener("DOMContentLoaded", function() {
    const reviewDisList = document.querySelectorAll(".Reviewed");
    const reviewCommentList = document.querySelectorAll(".review-menu-wrap");

    reviewDisList.forEach((review, index) => {
        review.addEventListener("click", function(event) {
            // Prevent default behavior of the link
            event.preventDefault();
            
            // Toggle the class 'open-menu' on the corresponding review comment list
            reviewCommentList[index].classList.toggle("open-menu");
        });

        // Clicking anywhere else on the document will close the review menu
        document.addEventListener("click", function(event) {
            if (!reviewCommentList[index].contains(event.target) && !reviewDisList[index].contains(event.target)) {
                reviewCommentList[index].classList.remove("open-menu");
            }
        });
    });
});

document.addEventListener("DOMContentLoaded", function() {
    var reviews = document.querySelectorAll(".review-message");
    reviews.forEach(function(review) {
      var rating = parseInt(review.querySelector(".rating-review").textContent); // Get the star rating as an integer
      var starsContainer = review.querySelector(".stars");
      starsContainer.innerHTML = ""; // Clear previous stars
  
      // Create filled stars based on the rating
      for (var i = 0; i < rating; i++) {
        var star = document.createElement("i");
        star.classList.add("star", "fas", "fa-star", "filled"); // Add filled class to each star
        starsContainer.appendChild(star);
      }
    });
  });


  // Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.querySelectorAll("deleteBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
function toggleModal() {
    modal.style.display = modal.style.display === "block" ? "none" : "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  toggleModal();
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    toggleModal();
  }
}

btns.forEach(function(btn) {
    btn.onclick = function() {
        // Find the corresponding post and delete it
        var postId = btn.dataset.postId; // Assuming postId is stored in data attribute
        deleteItem(postId);
    };
});

// Function to delete the item (to be implemented)
function deleteItem(postId) {
    // Implement deletion logic here
    toggleModal(); // Close the modal after deletion
}



document.addEventListener('DOMContentLoaded', function() {
    const connectLinks = document.querySelector('.connect-link');

    connectLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            const postContainer = event.target.closest('.post-container');
            const authorId = postContainer.dataset.postAuthorId;

            // Send authorId to backend
            fetch('/create_chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ authorId: authorId })
            })
            .then(response => response.json())
            .then(data => {
                // Handle response from backend
                console.log('Chat ID created:', data.chatId);
            })
            .catch(error => console.error('Error:', error));
        });
    });
});


// function loadConversationContent() {
//     // Make an AJAX request to fetch the latest conversation content from the server
//     fetch('/chats')
//         .then(response => response.text())
//         .then(data => {
//             // Update the content of the .conversation-main section
//             document.querySelector('.conversation-main').innerHTML = data;
//         })
//         .catch(error => {
//             console.error('Error loading conversation content:', error);
//         });
// }

// Call the function initially to load conversation content
// loadConversationContent();

// // Optionally, set an interval to refresh conversation content periodically
// // Adjust the interval duration as needed (e.g., every 5 seconds)
// setInterval(loadConversationContent, 5000); // Refresh every 5 seconds


// document.addEventListener("DOMContentLoaded", function() {
//     // Find the "Connect" link
//     var connectLink = document.getElementById("chat-link-creator");
  
//     // Add a click event listener
//     connectLink.addEventListener("click", function(event) {
//       // Prevent the default action (following the link)
//       event.preventDefault();
  
//       // Extract the post_id from the link's href attribute
//       var postId = connectLink.getAttribute("href").split("/").pop();
  
//       // Extract the id of the author of the post
//       var authorId = connectLink.closest(".post").getAttribute("data-author-id");
  
//       // Create a new form element
//       var form = document.createElement("form");
//       form.setAttribute("method", "POST");
//       form.setAttribute("action", "/create_chat");
  
//       // Create input fields for post_id and author_id
//       var postIdField = document.createElement("input");
//       postIdField.setAttribute("type", "hidden");
//       postIdField.setAttribute("name", "post_id");
//       postIdField.setAttribute("value", postId);
//       form.appendChild(postIdField);
  
//       var authorIdField = document.createElement("input");
//       authorIdField.setAttribute("type", "hidden");
//       authorIdField.setAttribute("name", "author_id");
//       authorIdField.setAttribute("value", authorId);
//       form.appendChild(authorIdField);
  
//       // Append the form to the document body and submit it
//       document.body.appendChild(form);
//       form.submit();
//     });
//   });
  