// Handle navigation between posts when 'h' or 'l' is pressed.
function handleNavigate(e) {
    if (e.altKey || e.ctrlKey || e.shiftKey || e.metaKey) {
        return;
    }

    var to = null;
    var cmd = String.fromCharCode(e.which).toLowerCase();

    switch (cmd) {
        case 'h':
            to = $("#next").attr("href");
            break;
        case 'l':
            to = $("#previous").attr("href");
            break;
    }

    if (to) {
        window.location.href = to;
    }
}

// Handle scrolling when 'j' or 'k' is pressed.
function handleScroll(e) {
    if (e.altKey || e.ctrlKey || e.shiftKey || e.metaKey) {
        return;
    }

    var speed = 10;
    var cmd = String.fromCharCode(e.which).toLowerCase();
    var pos = $(document).scrollTop();
    switch (cmd) {
        case 'j':
            $(document).scrollTop(pos + speed);
            break;
        case 'k':
            $(document).scrollTop(pos - speed);
            break;
    }
}

$(function() {
    // keypress events are level sensitive, so use them in case the
    // scrolling keys are held down instead of only pressed.
    $(document).keydown(handleNavigate).keypress(handleScroll);
});
