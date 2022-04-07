document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {

        initialView: 'dayGridMonth',
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay'
        },
        dateClick: function (info) {
            
        },

        events: [
            // {% for event in events %}
            {
                title: '{{event.todo}}',
                start: '{{event.date}}',
            },
            // {% endfor %}
        ]
    }
    );
    calendar.setOption('locale', 'ISO');
    calendar.render();
});