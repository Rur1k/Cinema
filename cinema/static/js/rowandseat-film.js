$(document).ready(function() {
        var source = document.querySelector(".js-selected-seat-template").innerHTML;
        var template = Handlebars.compile(source);
        var selectedSeats = {
            addedSeats: [],
            sum: 0
        };

        $('.js-seat-container').on('click', '.js-seat-selector', function(e) {
            var targetElem = e.currentTarget;
            var dataSet = targetElem.dataset;
            //var resultString = 'ряд:' + dataSet.seatRow + ' место:' + dataSet.seatCol;
            //console.log(resultString);
            var newSeat = {
                row: dataSet.seatRow,
                seat: dataSet.seatCol
            };
            var existingSeatIndex = -1;
            for(var i=0;i<selectedSeats.addedSeats.length;i++){
                var currentSeat = selectedSeats.addedSeats[i];
                if(currentSeat.row === newSeat.row && currentSeat.seat === newSeat.seat){
                    existingSeatIndex = i;
                    break;
                }
            }
            if(existingSeatIndex!==-1){
                selectedSeats.addedSeats.splice(existingSeatIndex, 1);
            }
            else {
                selectedSeats.addedSeats.push(newSeat);
            }

            var resultHtml = template(selectedSeats);
            $('.js-seat-result-container').html(resultHtml)
        });
    }
)