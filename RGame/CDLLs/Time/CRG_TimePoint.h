#pragma once


class CRG_TimePoint
{
public:
	double Difference(CRG_TimePoint*);
	void Increament(double);
	void Increament_s(long);
	void Increament_ms(long);
	void Increament_us(long);
	void Increament_ns(long);
	void Decreament(double);
	void Decreament_s(long);
	void Decreament_ms(long);
	void Decreament_us(long);
	void Decreament_ns(long);
	std::chrono::time_point<std::chrono::high_resolution_clock> _timePoint;
};


