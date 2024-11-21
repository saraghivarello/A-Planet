<script type="text/javascript" src="js-file.js"></script>

<script type="text/javascript">
$(function() {
    {% if view.timeout_seconds %}
      $('div#time-limit').show();
      var currentDate = new Date();
      var milliseconds = {{ view.remaining_timeout_seconds }}*1000;
      $('.glyphicon-time').after($('<span id="hours"></span>'))
      $('.glyphicon-time').after($('<span id="days"></span>'))
      $('span#minutes').css('margin-left','-3px')
      $('div#clock').countdown(currentDate.valueOf() + milliseconds, function(event) {

      switch(event.type) {
        case "seconds":
            $(this).find('span#seconds').html(event.value);
            break;
        case "minutes":
            if (event.lasting.minutes < 10){
                $(this).find('span#minutes').html('0' + event.lasting.minutes);
            } else {
                $(this).find('span#minutes').html(event.lasting.minutes);
            }
            break;
        case "hours":
            total_hours = event.lasting.days * 24 + event.lasting.hours;
            if (total_hours < 10) {
                $(this).find('span#hours').html('0' + total_hours +':');
            } else {
                $(this).find('span#hours').html(total_hours+':');
            }
            break;

        case "finished":
            $('#clock').hide(duration=0);
            $('#time-out-message').show(duration=0);
            $('<input>').attr({
                type: 'hidden',
                name: 'auto_submit',
                value: '1'
            }).appendTo('form');
            $('#form').submit();

            break;
          }
      });
    {% endif %}
});
</script>
