# IoT-FireGuard-Automated-Fire-Alert-and-Suppression-System
## Abstract
Fire Detectors play a very important role in Industries, Shops, Malls, Residential complexes, parking areas, etc. They help in detecting fire or smoke at an early stage and can help in saving lives. In this project, I have designed an IoT based Fire Alerting and Fighting System using Fire monitor which would not only signal the presence of fire in a particular premise but also take the necessary actions to avert the worst-case scenario.

## Apparatus Used
- Microcontroller (MCU-PT) or single-boarded computer.
- Fire Detectors
- LCD display
- Speaker
- Motorized shutter door
- Water Sprinkler

## Description
- **Microcontroller (MCU-PT) or single-boarded computer:** A microcontroller is a type of processor that traditionally was a scaled-down, all-in-one embedded processor, memory and I/O for use in very specific operations. The idea behind the microcontroller unit (MCU) is that it is cost-effective, energy-efficient processor that can be purpose-built for a specific application. Here it's used as the main brain of the entire project. All the commands to the other apparatus are given by this MCU.
- **Fire Detector:** It’s the main input apparatus used for this project, it detects the fire when it reaches a certain value then it sends the data about it to the MCU after that MCU sends the information to other apparatus to take the necessary action.
- **LCD display:** A liquid-crystal display (LCD) is a flat-panel display or other electronically modulated optical device that uses the light-modulating properties of liquid crystals combined with polarizers. In this project, LCD panel is used as an output device which alerts the people by displaying necessary messages. If no fire is detected then it prints the message “SAFE”, and in the time of fire emergency as per detected by the fire detector it prints the message ”FIRE DETECTED”.
- **Speaker:** It's one of the output devices used in the project to alert the people if a fire breaks out. It only turns on when fire is detected.
- **Motorized shutter door:** It’s a door which can be opened and closed manually, but if fire is detected, then it will open on its own as a safety measure.
- **Water Sprinkler:** It's also one of the output devices used in this project, which is set to get activated by MCU in case if fire is detected. It will get activated and sprinkle water on fire to cut the oxygen supply to the fire so that the fire spread can be stopped.

## Project Layout
![Fire Alert](https://github.com/AyanNaska/IoT-FireGuard-Automated-Fire-Alert-and-Suppression-System/assets/113054786/86967ef6-3dd7-40a9-8fa5-86b66d50ad80)

## Connections
- Fire Monitor from D0 to D0 on MCU
- Fire Sprinkler from D0 to D1 on MCU
- Emergency Door from D0 to D3 on MCU
- LCD Display from D0 to D4 on MCU
- Speaker from D0 to D2 on MCU

## Results
When the fire is not in the range of the fire detector then Door remains close, Sprinkler remains off, Speaker remains silent, LCD panel prints the result SAFE but as soon as the fire comes in the detection range of the fire monitor then Sprinkler turns on and sprinkles water, Door opens, Speakers turn on, LCD panel prints FIRE DETECTED.

##Demo
https://github.com/AyanNaska/IoT-FireGuard-Automated-Fire-Alert-and-Suppression-System/assets/113054786/c38b2218-efe2-49da-96b1-d72eced5b003

## Conclusion
According to the National Fire Protection Association (NFPA), fire departments respond to over 350,000 home structure fires a year nationwide, causing almost $7 billion in direct damage. Far more tragic than property destruction, is the more than 2,500 civilian fire deaths and 12,300 civilian fire injuries annually. This project cannot destroy the cause of these accidents but it’s the best thing we can have to fight fire accidents if it ever happens. This should be installed in every house, schools, colleges shops and especially in places where inflammable substances are there where chances of fire accidents are more.
