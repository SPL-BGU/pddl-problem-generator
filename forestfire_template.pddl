;; Alexander Shleyfman (shleyfman.alexander@gmail.com)
(define (problem ${instance_name})

	(:domain forestfire)

	(:objects
		${bots_list} - bot
		${axe_list} - axe
		${grass_plots} - grass
		${bushes_plots} - bushes
	)

  (:init
		${connected_grass_plots}
        ${boat_velocity}
		${people_d_position}

	)

	(:goal
		(and
			${people_to_save}
		)
	)
)

