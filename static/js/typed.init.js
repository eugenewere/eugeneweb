
// Typed Text
$(".element").each(function(){
        var $this = $(this);
        $this.typed({
        strings: $this.attr('data-elements').split(','),
        typeSpeed: 70, // typing speed
        backDelay: 500, // pause before backspacing
        smartBackspace: true,
    });
});