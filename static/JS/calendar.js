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
            $('#myModal').modal('show');
            var event = createEvent(info.dateStr, 'Some event', undefined);
            if (new Date(event.start) < new Date()) {
                alert("La fecha ya pasó")
            } else {
                calendar.addEvent(event);
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


function createEvent(startDate, title, endDate) {
    const event = {
        id: CreateUUID(), // You must use a custom id generator
        title: title,
        start: startDate,
        allDay: endDate ? endDate : true // If there's no end date, the event will be all day of start date
    }
    return event;
}

function CreateUUID() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
        var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
}