// All functions  ------------------
function initSpringbook() {
    "use strict";
    var n = $(".bg");
    n.each(function(a) {
        if ($(this).attr("data-bg")) $(this).css("background-image", "url(" + $(this).data("bg") + ")");
    });
	function catwidth() {
        var a = $(".category-nav-inner ul li").length;
        var b = $(".category-nav-inner").width();
        $(".category-nav-inner ul li").css({
            width: b / a   
        });
    }
	catwidth();
	$(window).on('load scroll', function () {
        var scrolled = $(this).scrollTop();
        $('.hero-bg .bg , .video-holder , .slideshow-slider').css('transform', 'translate3d(0, ' + +(scrolled * 0.25) + 'px, 0)');  
    });
	// magnificPopup ------------------
    $(".image-popup").magnificPopup({
        type: "image",
        closeOnContentClick: false,
        removalDelay: 600,
        mainClass: "my-mfp-slide-bottom",
        image: {
            verticalFit: false
        }
    });
    $(".popup-youtube, .popup-vimeo , .show-map").magnificPopup({
        disableOn: 700,
        type: "iframe",
        removalDelay: 600,
        mainClass: "my-mfp-slide-bottom"
    });
    $(".popup-gallery").magnificPopup({
        delegate: "a",
        type: "image",
        fixedContentPos: true,
        fixedBgPos: true,
        tLoading: "Loading image #%curr%...",
        removalDelay: 600,
        closeBtnInside: true,
        zoom: {
            enabled: true,
            duration: 700
        },
        gallery: {
            enabled: true,
            navigateByImgClick: true,
            preload: [ 0, 1 ]
        },
        image: {
            tError: '<a href="%url%">The image #%curr%</a> could not be loaded.'
        }
    });
	var mc = new Hammer(document.body);
    mc.on("swipeleft", function() {
        $(".mfp-arrow-left").magnificPopup("prev");
    });
    mc.on("swiperight", function() {
        $(".mfp-arrow-right").magnificPopup("next");
    });
	// Owl  ------------------
	var fwc = $(".full-width-carousel");
    fwc.owlCarousel({
        margin: 0,
        items: 1,
        smartSpeed: 1300,
        loop: true,
        dots: false,
        nav: false,
		center:true,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 2
            },
            1024: {
                items: 3
            }
        } 
 
    }) ;
    $(".full-width-carousel-holder a.next-slide").on("click", function() {
        $(this).closest(".full-width-carousel-holder").find(fwc).trigger("next.owl.carousel");
        return false;
    });
    $(".full-width-carousel-holder a.prev-slide").on("click", function() {
        $(this).closest(".full-width-carousel-holder").find(fwc).trigger("prev.owl.carousel");
        return false;
    });
    var slsl = $(".slideshow-slider");
    slsl.owlCarousel({
        loop: true,
        margin: 0,
        nav: false,
        items: 1,
        dots: false,
        autoHeight: false,
        animateOut: "fadeOut",
        animateIn: "fadeIn",
        autoplay: true,
        autoplayTimeout: 4000,
        autoplayHoverPause: false,
        autoplaySpeed: 3600
    });
	var csi = $(".full-width-slider")  , dup = $(".full-width-slider").data("attime") ;
    csi.owlCarousel({
        loop: true,
        margin: 0,
        nav: false,
        items: 1,
        dots: false,
		center: true,
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: dup,
        autoplayTimeout: 3000,
        autoplayHoverPause: false,
        autoplaySpeed: 2600,
        onInitialized: function(a) {
			$(".num-holder").text("1" + " / " + this.items().length);
        }
    	}).on("changed.owl.carousel", function(a) {
			var b = --a.item.index, a = a.item.count;
			$(".num-holder").text((1 > b ? b + a : b > a ? b - a : b) + " / " + a);
    });
    $(".full-width-slider-holder a.next-slide").on("click", function() {
        $(this).closest(".full-width-slider-holder").find(csi).trigger("next.owl.carousel");
        return false;
    });
    $(".full-width-slider-holder a.prev-slide").on("click", function() {
        $(this).closest(".full-width-slider-holder").find(csi).trigger("prev.owl.carousel");
        return false;
    });
	var ssc = $(".single-slider");
    ssc.owlCarousel({
        loop: true,
        margin: 0,
        nav: false,
        items: 1,
        dots: true,
		center: true,
        smartSpeed: 1200,
        autoHeight: false,
        onInitialized: function(a) {
            $(".num-holder2").text("1" + " / " + this.items().length);
        }
    }).on("changed.owl.carousel", function(a) {
        var b = --a.item.index, a = a.item.count;
        $(".num-holder2").text((1 > b ? b + a : b > a ? b - a : b) + " / " + a);
    });
    $(".single-slider-holder a.next-slide").on("click", function() {
        $(this).closest(".single-slider-holder").find(ssc).trigger("next.owl.carousel");
        return false;
    });
    $(".single-slider a.prev-slide").on("click", function() {
        $(this).closest(".single-slider-holder").find(ssc).trigger("prev.owl.carousel");
        return false;
    });
    function aht() {
        $(".slideshow-slider .item").css({
            height: $(".slideshow-slider").outerHeight(true)
        });
 
    }
    aht();
	$(window).resize(function() {
	catwidth();
	 aht();
	
 		var ww4 = $(window).width();
		if( ww4 < 1024){
			$('.top-bar-menu').css('display','none')		
		}
		else if (ww4 > 1024){
			$('.top-bar-menu').css('display','block')			
		}
    });
	$(".to-top").on("click", function() {
        $("html, body").animate({
            scrollTop: 0
        }, {
            queue: false,
            duration: 1200
        });
		  return false;
    });
	$(window).on("scroll", function(a) {
		var ttop = $(".to-top"),
			ttopi = $(".top-bar-info"),
			tob = $("#top-bar"),
			fil = $(".fixed-icons li");
			
		if ($(this).scrollTop() > 90){
		ttop.fadeIn(500); 
		ttopi.slideUp(500); 
		tob.addClass("get-sticky");
		$(".fixed-icons li").addClass("showic");
		}
	 else{ 
		ttop.fadeOut(500);
		ttopi.slideDown(500); 
		tob.removeClass("get-sticky");
		fil.removeClass("showic"); 
		}
	});
 	$('#hid-men').menu();
	$(".sb-to-top").on("click", function() {
        $(".fixed-sidebar").animate({
            scrollTop: 0
        }, {
            queue: false,
            duration: 1200
        });
		  return false;
    });
	$(".sh-hid-sb").on("click", function() {
		$("html, body").addClass("hidhtml")
		$(".sb-overlay").fadeIn(500);
        $(".fixed-sidebar").animate({
           right: 0
        }, {
            queue: false,
            duration: 500
        });
		
	});
	$(".close-sibedar , .sb-overlay").on("click", function() {
		$("html, body").removeClass("hidhtml")
		$(".sb-overlay").fadeOut(500);
 
        $(".fixed-sidebar").animate({
           right:  - 350 + "px"
        }, {
            queue: false,
            duration: 500
        });
		
	});	
	$(".searchform input").on('keypress change', function(event) {
       var data=$(this).val();
       $(".dublicated-text").text(data);
	});	
	$(".close-fixed-search , .search-form-bg").on("click", function() {
		$(".fixed-search").fadeOut(300);
	});
	$(".show-fixed-search").on("click", function() {
		$(".fixed-search").fadeIn(300);
	});
	// isotope ------------------
    function initisotop() {
        if ($(".grid-sb-holder").length) {
            var a = $(".grid-sb-holder").isotope({
                singleMode: true,
                columnWidth: ".grid-sb-wrap",
                itemSelector: ".grid-sb-wrap"
            });
            a.imagesLoaded(function() {
                a.isotope("layout");
            });
            $(".gallery-filters").on("click", "a.gallery-filter", function(b) {
                b.preventDefault();
                var c = $(this).attr("data-filter");
                a.isotope({
                    filter: c
                });
                $(".gallery-filters a.gallery-filter").removeClass("gallery-filter-active");
                $(this).addClass("gallery-filter-active");
                return false;
            });
        }
    }
    initisotop();
// Share ------------------
    var shs = eval($(".share-container").attr("data-share"));
    $(".share-container").share({
        networks: shs
    });
	$(".share-button").on("click", function() {
		$(".share-inner").toggleClass("is-share")
	});
    $(".art-facts").scrollToFixed({
        minWidth: 1036,
		removeOffsets: true,
		 marginTop: $('#top-bar').outerHeight() - 40,
		 limit: function() {
            var a = $('.limit-box').offset().top - $('.art-facts').outerHeight(true) - 10;
            return a;
        },
 
    });
    $(".sticky-nav-holder").scrollToFixed({
        minWidth: 1036,
		removeOffsets: true,
		zIndex: 21,
    });

    var l = $(".background-youtube").data("vid");
    var m = $(".background-youtube").data("mv");
    $(".background-youtube").YTPlayer({
        fitToBackground: true,
        videoId: l,
        pauseOnScroll: true,
        mute: m,
        callback: function() {
            var a = $(".background-video").data("ytPlayer").player;
        }
    });
    var vid = $(".background-vimeo").data("vim");
    $(".background-vimeo").append('<iframe src="//player.vimeo.com/video/' + vid + '?background=1"  frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen ></iframe>');
    $(".video-holder").height($(".media-container").height());
    if ($(window).width() > 1024) {
        if ($(".video-holder").size() > 0) if ($(".media-container").height() / 9 * 16 > $(".media-container").width()) {
            $(".background-vimeo iframe ").height($(".media-container").height()).width($(".media-container").height() / 9 * 16);
            $(".background-vimeo iframe ").css({
                "margin-left": -1 * $("iframe").width() / 2 + "px",
                top: "-75px",
                "margin-top": "0px"
            });
        } else {

            $(".background-vimeo iframe ").width($(window).width()).height($(window).width() / 16 * 9);
            $(".background-vimeo iframe ").css({
                "margin-left": -1 * $("iframe").width() / 2 + "px",
                "margin-top": -1 * $("iframe").height() / 2 + "px",
                top: "50%"
            });
        }
    } else if ($(window).width() < 760) {
        $(".video-holder").height($(".media-container").height());
        $(".background-vimeo iframe ").height($(".media-container").height());
    } else {
        $(".video-holder").height($(".media-container").height());
        $(".background-vimeo iframe ").height($(".media-container").height());
    }
 
	$('.video-container').css('width', $(window).width()+'px');
	$('.video-container ').css('height', parseFloat(720/1280*$(window).width())+'px');
	if($('.video-container').height()<$(window).height()) {
		$('.video-container ').css('height', $(window).height()+'px');
		$('.video-container').css('width', parseFloat(1280/720*$(window).height())+'px');
	}
	$(".menubutton").on("click", function() {
		$(".top-bar-menu").slideToggle(300);	
	});
	$(".cat-button").on("click", function() {
		$(".category-nav-inner ul").slideToggle(300);
	});
}
// Init all functions------------------
$(document).ready(function() {
    initSpringbook();
});