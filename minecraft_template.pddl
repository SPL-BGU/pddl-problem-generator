;; Benyamin et al. 2024 (https://github.com/SPL-BGU/PDDL-Minecraft), basic PDDL version (item counts model) of the Pogo Stick problem in Polycraft Minecraft domain.

(define (problem ${instance_name})
	(:domain polycraft)

  (:init
		${trees_in_map_initial}
		${count_log_in_inventory_initial}
		${count_planks_in_inventory_initial}
		${count_stick_in_inventory_initial}
		${count_sack_polyisoprene_pellets_in_inventory_initial}
		${count_tree_tap_in_inventory_initial}
        (= (count_wooden_pogo_stick_in_inventory) 0)
	)
	(:goal
		(and
			(>= (count_wooden_pogo_stick_in_inventory) 1)
		)
	)
)

