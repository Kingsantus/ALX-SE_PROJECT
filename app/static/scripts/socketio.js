const socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on('connect', () => {
    console.log('Connected to Socket.IO server');
});


// Add an event listener for the form submission
document.querySelector('.conversation-form-submit').addEventListener('click', function() {
    const content = document.querySelector('.conversation-form-input').value;
    const chatId = this.closest('.conversation').id.split('--')[1];
    const now = new Date;
    const hours = now.getHours().toString().padStart(2, '0'); // Get hours (0-23) and pad with leading zero if needed
    const minutes = now.getMinutes().toString().padStart(2, '0'); // Get minutes and pad with leading zero if needed
    const timestamp = `${hours}:${minutes}`; // Format the timestamp as "HH:MM"

    
    // Emit a 'send_message' event to the server with message content and chat ID
    if (content !== '') {
        socket.emit('send_message', {content: content, chat_id: chatId, timestamp: timestamp});
    }
    document.querySelector('.conversation-form-input').value = '' 
});

// Handle received messages from the server
// Handle received messages from the server
socket.on('receive_message', function(data) {
    // Append the new message to the conversation
    var conversationWrapper = document.querySelector('.conversation-wrapper');
    var messageItem = document.createElement('li');
    messageItem.className = 'conversation-item me';
    messageItem.innerHTML = `
        <div class="conversation-item-side">
            <img src="${data.user_image_file}" class="conversation-item-image">
        </div>
        <div class="conversation-item-content">
            <div class="conversation-item-wrapper">
                <div class="conversation-item-box">
                    <div class="conversation-item-text">
                        <p>${data.content}</p>
                        <span class="conversation-item-time">${data.timestamp}</span>
                    </div>
                    <div class="conversation-item-dropdown">
                        <button type="button" class="conversation-item-dropdown-toggle"><i class="ri-more-2-line"></i></button>
                        <ul class="conversation-item-dropdown-list">
                            <li><a href="#"><i class="ri-share-forward-line"></i>Forward</a></li>
                            <li><a href="#"><i class="ri-delete-bin-line"></i>Delete</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    `;
    conversationWrapper.appendChild(messageItem);
});