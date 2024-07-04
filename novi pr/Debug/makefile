################################################################################
# Automatically-generated file. Do not edit!
################################################################################

-include ../makefile.init

RM := rm -rf

# All of the sources participating in the build are defined here
-include sources.mk
-include Drivers/STM32F1xx_HAL_Driver/Src/subdir.mk
-include Core/Startup/subdir.mk
-include Core/Src/subdir.mk
-include subdir.mk
-include objects.mk

ifneq ($(MAKECMDGOALS),clean)
ifneq ($(strip $(C_DEPS)),)
-include $(C_DEPS)
endif
endif

-include ../makefile.defs

# Add inputs and outputs from these tool invocations to the build variables 
EXECUTABLES += \
novi\ pr.elf \

SIZE_OUTPUT += \
default.size.stdout \

OBJDUMP_LIST += \
novi\ pr.list \

OBJCOPY_HEX += \
novi\ pr.hex \

OBJCOPY_BIN += \
novi\ pr.bin \


# All Target
all: novi\ pr.elf secondary-outputs

# Tool invocations
novi\ pr.elf: $(OBJS) $(USER_OBJS) C:\Users\Pavle\Desktop\novi\ pr\STM32F103C6TX_FLASH.ld
	arm-none-eabi-gcc -o "novi pr.elf" @"objects.list" $(USER_OBJS) $(LIBS) -mcpu=cortex-m3 -T"C:\Users\Pavle\Desktop\novi pr\STM32F103C6TX_FLASH.ld" --specs=nosys.specs -Wl,-Map="novi pr.map" -Wl,--gc-sections -static --specs=nano.specs -mfloat-abi=soft -mthumb -Wl,--start-group -lc -lm -Wl,--end-group
	@echo 'Finished building target: $@'
	@echo ' '

default.size.stdout: $(EXECUTABLES)
	arm-none-eabi-size  $(EXECUTABLES)
	@echo 'Finished building: $@'
	@echo ' '

novi\ pr.list: $(EXECUTABLES)
	arm-none-eabi-objdump -h -S $(EXECUTABLES) > "novi pr.list"
	@echo 'Finished building: $@'
	@echo ' '

novi\ pr.hex: $(EXECUTABLES)
	arm-none-eabi-objcopy  -O ihex $(EXECUTABLES) "novi pr.hex"
	@echo 'Finished building: $@'
	@echo ' '

novi\ pr.bin: $(EXECUTABLES)
	arm-none-eabi-objcopy  -O binary $(EXECUTABLES) "novi pr.bin"
	@echo 'Finished building: $@'
	@echo ' '

# Other Targets
clean:
	-$(RM) *
	-@echo ' '

secondary-outputs: $(SIZE_OUTPUT) $(OBJDUMP_LIST) $(OBJCOPY_HEX) $(OBJCOPY_BIN)

.PHONY: all clean dependents
.SECONDARY:

-include ../makefile.targets
