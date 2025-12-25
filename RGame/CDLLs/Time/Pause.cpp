#include "pch.h"
#include "Pause.h"

//extern "C" {     __declspec(dllexport) Foo* Foo_new() { return new Foo(); }     ) void Foo_bar(Foo* foo) { foo->bar(); } }

extern "C" __declspec(dllexport) void Pause(double);
extern "C" __declspec(dllexport) void PauseUntil(CRG_TimePoint*);

void Pause(double time)
{
	auto timeTill = std::chrono::high_resolution_clock::now() + std::chrono::duration<double,std::nano>(time*1000000000);
	while (true)
	{
		if (timeTill <= std::chrono::high_resolution_clock::now())return;
		_mm_pause();
	}
}
void PauseUntil(CRG_TimePoint time) 
{
	if (time._timePoint >= std::chrono::high_resolution_clock::now()) return;
	while (true)
	{
		if (time._timePoint <= std::chrono::high_resolution_clock::now())return;
		_mm_pause();
	}
}