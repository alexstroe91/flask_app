
document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');


    var calendar = new FullCalendar.Calendar(calendarEl, {

        events:[
            {
              title: "Titulo",
              start: "2022-04-11"
            }
          ],

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

                $('#myModal').modal('show');
            }
        },

        eventClick: function (info) {
            evento = calendar.getEventById(info.event.id);

            if (confirm("Eliminar evento") == true) {
                evento.remove();
            }

        }
    }
    );
    calendar.setOption('locale', 'ISO');
    calendar.render();
});


function createEvent(title, endDate, startTime, endTime, date) {
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