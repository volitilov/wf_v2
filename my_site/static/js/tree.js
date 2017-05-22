var j = jQuery.noConflict();

j(function() {
    j('.widjet-tree .dropdown > a').click(function(event) {
        event = event || window.event;
        event.preventDefault();

        var togle = j(this).next();

        if (togle.css('display') == 'none') {
            j(this).find('i').css({
                transform: 'rotate(180deg)'
            });
            togle.show();
        } else {
            j(this).find('i').css({
                transform: ''
            });
            togle.hide();
        }

        return false;
    });

});