schedulers:

|operator|scheduler|_scheduler|forwarding|composed|depends|
|-- |-- |-- |-- |-- |-- |
|amb|-|-|X|-||
|as_observable|-|-|X|-||
|average|-|-|-|X||
|buffer|-|-|?|X|window*, flat_map|
|buffer_when|-|-|?|X|window*, flat_map,|
|buffer_toggle|-|-|?|X|window*, flat_map|
|buffer_with_count|-|-|?|X|window*, flat_map, filter, map, to_terable|
|buffer_with_time|X|-|?|X|window*, flat_map|
|buffer_with_time_or_count|X|-|?|X|window*, flat_map|
|?|?|?|?|?||
|?|?|?|?|?||
|?|?|?|?|?||
|?|?|?|?|?||


