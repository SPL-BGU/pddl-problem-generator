(define (problem ${instance_name})

	(:domain expedition)

	(:objects
		${sleds_list} - sled
		${waypoint_list} - waypoint
	)

  (:init
		${sleds_initial_positions}
        ${sleds_capacity}
		${sleds_supplies}
		${waypoint_supplies}
        ${waypoints_connections}
	)

	(:goal
		(and
			${sleds_goal_positions}
		)
	)
)

