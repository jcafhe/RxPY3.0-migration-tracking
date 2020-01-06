schedulers:

|operator|scheduler|_scheduler|forwarding|composed|depends|
|-- |-- |-- |-- |-- |-- |
|amb|-|-|X|-||
|as_observable|-|-|X|-||
|average|-|-|X|X||
|buffer|-|-|X|X|window*, flat_map|
|buffer_when|-|-|X|X|window*, flat_map,|
|buffer_toggle|-|-|X|X|window*, flat_map|
|buffer_with_count|-|-|X|X|window*, flat_map, filter, map, to_terable|
|buffer_with_time|X|-|X|X|window*, flat_map|
|buffer_with_time_or_count|X|-|X|X|window*, flat_map|
|catch::catch_handler|-|-|X|-||
|catch::rx.catch|-|-|X|X|rx.catch|
|combine_latest|-|-|X|X|rx.combine_latest|
|concat|-|-|X|X|rx.concat|
|contains|-|-|X|X|filter, some|
|count|-|-|X|X|filter, reduce, count|
|debounce|X|X|?|?||
|throttle_with_mapper|-|-|X|-||
|?|?|?|?|?||
|?|?|?|?|?||
|?|?|?|?|?||
|?|?|?|?|?||
|?|?|?|?|?||
|?|?|?|?|?||
|?|?|?|?|?||
|?|?|?|?|?||
|?|?|?|?|?||

