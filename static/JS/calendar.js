
document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');


    var calendar = new FullCalendar.Calendar(calendarEl, {        
        


        displayEventTime: true,
        editable: true,
        initialView: 'dayGridMonth',
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay,listMonth'
        },
        
        
        dateClick: function (info) {
            if (info.date < new Date()) {
                alert("La fecha ya pasó")
            } else {
                clickedDate = new Date((info.date))
                clickedDate.setDate(clickedDate.getDate() + 1)
                document.getElementById("startDate").value = clickedDate.toISOString().split('T')[0]
                $('#addModal').modal('show');

            }
        },

        eventClick: function (info) {
            evento = calendar.getEventById(info.event.id);
            inicio = evento.start.toISOString().split('T')[0]
            alert(inicio)

            $('#changeModal').on('show.bs.modal',function(){
                $("#changeTitle").val(evento.title);
                //  $("#changeEndDate").val();
                // $("#changeStartTime").val();
                // $("#changeEndTime").val();
            });
            $('#changeModal').modal('show');

            // if (confirm("Eliminar evento") == true) {
            //     evento.remove();
            // }
        }
    }
    );
    calendar.setOption('locale', 'ISO');
    calendar.addEventSource("/eventos");
    calendar.render();
});

