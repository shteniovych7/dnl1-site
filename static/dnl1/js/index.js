$('.owl-one').owlCarousel({
    center: true,
    smartSpeed :900,
    loop:true,
    margin:0,
    items:1,
    dots:true,
    nav:true,
    navText : ["<i class='fa fa-chevron-left'></i>","<i class='fa fa-chevron-right'></i>"]
});

$('.owl-two').owlCarousel({
    loop:false,
    navText : ["<i class='fa fa-chevron-left'></i>","<i class='fa fa-chevron-right'></i>"],
    margin:20,
    responsive:{
        0:{
          items:1
        },
        576:{
          items:2
        },
        1024:{
          items:3
        }
    },
    nav:true,
    dots: true
});