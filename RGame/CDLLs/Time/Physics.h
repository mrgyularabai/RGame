#pragma once
#include <vector>
#include <chrono>

class CRG_Physics 
{
public:
	CRG_Physics(void (*mainSrcTick)(double), double interval, char* name)
	{
		LastTick = std::chrono::high_resolution_clock::now();
		_interval = interval;
		_interval_ns = (long long)(1000000000 * interval);
		_mainSrcTick = mainSrcTick;
		_name = name;
		_run = false;
	}
	void Start();
	void End();
	void Add(void(*obj) (double));
	bool Exists(void(*obj) (double));
	void Remove(void(*obj) (double));
	bool Running();
	double GetInterval();
	void SetInterval(double);
	double GetDeltaTime();
	long long GetCounter();
private:
	std::thread phythread;
	std::vector< void(*)(double) > _physicsList;
	void (*_mainSrcTick)(double);
	void (*testTick)(double);
	double _interval;
	double _waitLimit;
	long long _interval_ns;
	long long _counter;
	std::string _name;
	bool _run;
	std::chrono::time_point<std::chrono::high_resolution_clock> LastTick;
private:
	void Wait();
	static void Loop(CRG_Physics& p);
	void sleep(long long);
};



extern "C"
{
	__declspec(dllexport) CRG_Physics* New_CRG_Physics(void (*mainSrcTick)(double), double interval, char* name)
	{
		return new CRG_Physics(mainSrcTick, interval, name);
	};
	__declspec(dllexport) void Del_CRG_Physics(CRG_Physics* Tis)
	{
		delete Tis;
	};

	__declspec(dllexport) void CRG_Physics_Start(CRG_Physics* Tis) { Tis->Start();
	};
	__declspec(dllexport) void CRG_Physics_End(CRG_Physics * Tis) { Tis->End(); };
	__declspec(dllexport) void CRG_Physics_Add(CRG_Physics * Tis, void(*obj) (double)) { Tis->Add(obj); };
	__declspec(dllexport) void CRG_Physics_Remove(CRG_Physics * Tis, void(*obj) (double)) { Tis->Remove(obj); };
	__declspec(dllexport) bool CRG_Physics_Exists(CRG_Physics * Tis, void(*obj) (double)) { return Tis->Exists(obj); };
	__declspec(dllexport) bool CRG_Physics_Running(CRG_Physics * Tis) { return Tis->Running(); };
	__declspec(dllexport) double CRG_Physics_GetInterval(CRG_Physics * Tis) { return Tis->GetInterval(); };
	__declspec(dllexport) void CRG_Physics_SetInterval(CRG_Physics * Tis, double duration) { Tis->SetInterval(duration); };
	__declspec(dllexport) long long CRG_Physics_GetCounter(CRG_Physics * Tis) { return Tis->GetCounter(); };
	__declspec(dllexport) double CRG_Physics_GetDeltaTime(CRG_Physics * Tis) { return Tis->GetDeltaTime(); };
}