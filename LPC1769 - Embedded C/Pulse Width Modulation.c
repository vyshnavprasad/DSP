#include "LPC17xx.h"
#include "functions.h"
#define MAX_DAC_VALUE 1023
#define SAMPLE_TIME 10000

void PWM_Pulse(uint32_t);
void writetodac(uint32_t);
void init_IO_modules(void);
void wait_for_ADC_sample(void);

int main(void){
	int32_t ADCin;
	init_IO_modules();
	while(1){
		LPC_ADC->ADCR = LPC_ADC->ADCR | (uint32_t)1 << 24;
		wait_for_ADC_sample();
		ADCin = (LPC_ADC->ADGDR >> 4) & (uint32_t)0xFFF;
		ADCin = ADCin >> 2;
		PWM_Pulse(ADCin)
	}
	return 0;
}

void PWM_Pulse(uint32_t amp){
	uint32_t idx;
	uint32_t HIGH;
	uint32_t LOW;
	HIGH = uint32_t(SAMPLE_TIME*(amp/1024));
	writetodac(512);
	for(idx=0;idx<HIGH;idx++);

	LOW = SAMPLE_TIME - HIGH;
	writetodac(100);
	for(idx=0;idx<LOW;idx++);
}
	// extern uint32_t sinetable[];
	// extern int tableLen;
	// int count;
	// while(!wave){
	// 	for(count=0;count<tableLen;count++)
	// 	{
	// 		writetodac(sinetable[count]);
	// 		for(idx=0;idx<soft_delay;idx++);
	// 	}
	// }
// }

void writetodac(uint32_t value){
	uint32_t temp = 0;
	if(value > MAX_DAC_VALUE)
		value = MAX_DAC_VALUE;
	uint32_t DACR_VALUE_MASK=~((uint32_t)0x3FF<<6);
	temp = LPC_DAC->DACR & DACR_VALUE_MASK;
	LPC_DAC->DACR = (temp|value<<6);
}

void init_IO_modules(void)
{
	init_ADC();
	init_DAC();
	configure_OutputPin();
}

void wait_for_ADC_sample(void)
{
	uint32_t done;
	done = (LPC_ADC->ADGDR >> 31) & (uint32_t)1;
	while (!done)
	{
		done = (LPC_ADC->ADGDR >> 31) & (uint32_t)1;
	}
}