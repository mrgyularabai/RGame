#include "pch.h"
#include "CRG_TimePoint.h"

double RL_TimePoint::Difference( CRG_TimePoint* other)
{
	using namespace std::chrono;
	return duration<double>(_timePoint-(other->_timePoint)).count();
}

void RL_TimePoint::Increament(double time)
{

    double nanoSec = 0.000000001;

    if (time == 0) return;
    if (time < 0) Decreament(time*-1);
    if (time < nanoSec)return;

    using namespace std::this_thread; // sleep_for, sleep_until
    using namespace std::chrono; // nanoseconds, system_clock, seconds

    if (time - std::floor(time) < nanoSec)
    {
        Increament_s((int)std::floor(time));
        return;
    }

    time, nanoSec *= 1000;

    if (time - std::floor(time) < nanoSec)
    {
        Increament_ms((int)std::floor(time));
        return;
    }

    time, nanoSec *= 1000;

    if (time - std::floor(time) < nanoSec)
    {
        Increament_us((int)std::floor(time));
        return;
    }

    time, nanoSec *= 1000;

    if (time - std::floor(time) < nanoSec)
    {
        Increament_ns((int)std::floor(time));
        return;
    }
}

void CRG_TimePoint::Increament_s(long time)
{
    _timePoint += std::chrono::seconds();
}

void CRG_TimePoint::Increament_ms(long time)
{
    _timePoint += std::chrono::seconds();
}

void CRG_TimePoint::Increament_us(long time)
{
    _timePoint += std::chrono::seconds();
}

void CRG_TimePoint::Increament_ns(long time)
{
    _timePoint += std::chrono::seconds();
}

void CRG_TimePoint::Decreament(double time)
{

    double nanoSec = 0.000000001;

    if (time == 0) return;
    if (time < 0) Increament(time * -1);
    if (time < nanoSec)return;

    using namespace std::this_thread; // sleep_for, sleep_until
    using namespace std::chrono; // nanoseconds, system_clock, seconds

    if (time - std::floor(time) < nanoSec)
    {
        Decreament_s((int)std::floor(time));
        return;
    }

    time, nanoSec *= 1000;

    if (time - std::floor(time) < nanoSec)
    {
        Decreament_ms((int)std::floor(time));
        return;
    }

    time, nanoSec *= 1000;

    if (time - std::floor(time) < nanoSec)
    {
        Decreament_us((int)std::floor(time));
        return;
    }

    time, nanoSec *= 1000;

    if (time - std::floor(time) < nanoSec)
    {
        Decreament_ns((int)std::floor(time));
        return;
    }
}

void CRG_TimePoint::Decreament_s(long time)
{
    _timePoint -= std::chrono::seconds(time);
}

void CRG_TimePoint::Decreament_ms(long time)
{
    _timePoint -= std::chrono::milliseconds(time);
}

void CRG_TimePoint::Decreament_us(long time)
{
    _timePoint -= std::chrono::microseconds(time);
}

void CRG_TimePoint::Decreament_ns(long time)
{
    _timePoint -= std::chrono::nanoseconds(time);
}