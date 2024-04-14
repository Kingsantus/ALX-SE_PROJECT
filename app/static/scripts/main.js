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

