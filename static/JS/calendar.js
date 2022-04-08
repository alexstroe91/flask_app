document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');


    var calendar = new FullCalendar.Calendar(calendarEl, {
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
                $('#myModal').modal('show');
                
                // $('#myModal').on('hidden.bs.modal', function(){
                //     var titulo = $('#myModal-title').val();
                //     var endDate = $('#myModal').data('endDate');
                //     var startTime = $('#myModal').data('startTime');
                //     var endTime = $('#myModal').data('endTime');
                //     alert(titulo)
                //     evento = createEvent(titulo,endDate, startTime,endTime, info.date)

                //     calendar.addEvent(evento);
                // });
                

            }


            

        },

        eventClick: function (info) {
            evento = calendar.getEventById(info.event.id);
            evento.remove();
        }

    }
    );
    calendar.setOption('locale', 'ISO');
    calendar.render();
});


document.getElementById("endDate").setAttribute("min", new Date()); 

function createEvent(title,endDate,startTime,endTime, date) {
    const event = {
        id: CreateUUID(), // You must use a custom id generator
        title: title,
        start: date,
        end: endDate,
        startTime: startTime,
        endTime: endTime
    }
    return event;
}

function CreateUUID() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
        var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
}