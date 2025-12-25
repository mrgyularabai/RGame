#include "RL_Timer.h"
#include <chrono>

void RL_Timer::Now()
{
	_timePoint = std::chrono::steady_clock::now();
}

double RL_Timer::Diff()
{
	auto now = std::chrono::steady_clock::now();
	auto diff = std::chrono::duration_cast<std::chrono::microseconds>(now - _timePoint);
	return diff.count();
}
