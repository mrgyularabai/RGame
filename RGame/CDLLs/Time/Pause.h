#pragma once
#include <chrono>
#include "CRG_TimePoint.h"

extern "C" __declspec(dllexport) void Pause(double);
extern "C" __declspec(dllexport) void PauseUntil(CRG_TimePoint*);
