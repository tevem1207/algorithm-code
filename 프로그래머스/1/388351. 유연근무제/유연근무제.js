function solution(schedules, timelogs, startday) {
    return schedules.reduce((a, schedule, i) => a + getIsSuccess(timelogs[i], schedule, startday), 0);
}

const getIsSuccess = (timelog, schedule, startday) => {
    const scheduleMin = getMinutes(schedule);

    return timelog
        .every((time, i) => getMinutes(time) - scheduleMin <= 10 || (i + startday - 1) % 7 >= 5);
}

const getMinutes = (time) => {
    return Math.floor(time / 100) * 60 + time % 100
}