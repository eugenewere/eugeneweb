// Portfolio
//     $(window).on('load', function () {
        var $container = $('.portfolioContainer');
        $container.isotope({
            filter: '*',
            animationOptions: {
                duration: 750,
                easing: 'linear',
                queue: false
            }
        });

        $('.portfolioFilter a').click(function () {
            $('.portfolioFilter .active').removeClass('active');
            $(this).addClass('active');

            var selector = $(this).attr('data-filter');
            $container.isotope({
                filter: selector,
                animationOptions: {
                    duration: 750,
                    easing: 'linear',
                    queue: false
                }
            });
            return false;
        });

        var qsRegex;

        // init Isotope
        $container.isotope({
          filter: function() {
            return qsRegex ? $(this).text().match( qsRegex ) : true;
          }
        });

        // use value of search field to filter
        var $quicksearch = $('#mysearch').keyup( debounce( function() {
            // console.log($qui/cksearch.val());
          qsRegex = new RegExp( $quicksearch.val(), 'gi' );
          $container.isotope();
        }, 200 ) );

        // debounce so filtering doesn't happen every millisecond
        function debounce( fn, threshold ) {
              var timeout;
              threshold = threshold || 100;
              return function debounced() {
                clearTimeout( timeout );
                var args = arguments;
                var _this = this;
                function delayed() {
                  fn.apply( _this, args );
                }
                timeout = setTimeout( delayed, threshold );
              };
            }
    // });