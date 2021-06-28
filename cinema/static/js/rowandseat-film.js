$(document).ready(function() {
        $('.js-seat-container').on('click', '.js-seat-selector', function(e) {
            var targetElem = e.currentTarget;
            var dataSet = targetElem.dataset;
            var resultString = 'ряд:' + dataSet.seatRow + ' место:' + dataSet.seatCol;
            //console.log(resultString);
            $('.js-seat-result-container').append('<div>'+resultString+'</div>')
        });
    }
)