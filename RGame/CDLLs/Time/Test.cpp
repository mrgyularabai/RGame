#include "pch.h"
#include "Pause.h"
#include "CRG_TimePoint.h"

extern "C" __declspec(dllexport) void test();

void test()
{
	auto temp = new CRG_TimePoint();
	temp->_timePoint = std::chrono::high_resolution_clock::now();
	Pause(0.5);
	auto temp2 = new CRG_TimePoint();
	temp2->_timePoint = std::chrono::high_resolution_clock::now();

	std::cout << temp2->Difference(temp);
}