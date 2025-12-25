#include "pch.h"
#include "Physics.h"
#include "Pause.h"

/*void CRG_Physics::InitSleep()
{

}*/

void CRG_Physics::sleep(long long time) 
{
	auto timeTill = std::chrono::high_resolution_clock::now() + std::chrono::nanoseconds(time);
	while (true)
	{
		if (timeTill <= std::chrono::high_resolution_clock::now())return;
		_mm_pause();
	}
}

void CRG_Physics::Start() 
{
	_run = true;
	(*_mainSrcTick)(GetDeltaTime());
	LastTick = std::chrono::high_resolution_clock::now();
	(*_mainSrcTick)(GetDeltaTime());
	_waitLimit = std::chrono::duration<double,std::ratio<1,1>>(std::chrono::high_resolution_clock::now()-LastTick).count();
	
	//phythread = std::thread(Loop, std::reference_wrapper<CRG_Physics>(*this));
	Loop(*this);
}

void CRG_Physics::Loop(CRG_Physics& p)
{
	while (p._run)
	{
		auto lastTick = std::chrono::high_resolution_clock::now();
		p._counter++;
		(*p._mainSrcTick)(p.GetDeltaTime());
		for (int x = 0; x < p._physicsList.size(); x++)
		{
			(p._physicsList[x])(p.GetDeltaTime());
		}
		if (p._interval > p._waitLimit) p.sleep(p._interval_ns);
		p.LastTick = lastTick;
	}
}

double CRG_Physics::GetDeltaTime() 
{
	double difference = std::chrono::duration<double,std::nano>(std::chrono::high_resolution_clock::now() - LastTick).count();
	double result = difference/_interval_ns  ;
	return result;
}

void CRG_Physics::Wait() 
{
	
}

void CRG_Physics::End() 
{
	_run = false;
}

//getters and setters.
//getters.

double CRG_Physics::GetInterval() 
{
	return _interval;
}

bool CRG_Physics::Running() 
{
	return _run;
}

bool CRG_Physics::Exists(void(*obj) (double))
{
	for (auto check : _physicsList)
	{
		if (check == obj)return true;
	}
	return false;
}

long long CRG_Physics::GetCounter() 
{
	return _counter;
}

//setters

void CRG_Physics::SetInterval(double newinterval) 
{
	_interval = newinterval;
	_interval_ns = (long long)(_interval * 1000000000);
}

void CRG_Physics::Add(void(*obj) (double))
{
	_physicsList.emplace_back(obj);
}

void CRG_Physics::Remove(void(*obj) (double))
{
	_physicsList.erase(std::remove(_physicsList.begin(), _physicsList.end(), obj), _physicsList.end());
}
